from django.shortcuts import render
from .models import *
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.files import File
from .core import CoreAttendanceData
from django.http import HttpResponse
import datetime as dt


from .detectface import detect

# Create your views here.
def home(request):
    return render(request, 'attendance/homepage.html')

def traindata(request):
    return render(request, 'attendance/traindata.html')


def doattendance(request):
    url = 'attendance/temporarydata.txt'

    f = open(url, 'r')

    now = dt.datetime.now()
    # print(now.date())
    # print(now.time())

    listData = []

    for i in f:
        data = i.split('#')
        id = data[0]
        name = data[1]
        date = data[2]
        time = data[3]

        student = Student.objects.get(binusianID=id)

        #
        q = ClassSchedule.objects.filter(studentID = student).filter(date = now.date())

        if(q.count() != 0):
            q = q.first()
            print(q.getStartTime())
            print(q.getEndTime())
            print(now.time())
            print("-------------")
            if(q.getStartTime() <= now.time() and q.getEndTime() >= now.time()):
                check = AttendanceData.objects.filter(classScheduleID = q)
                if(check.count() == 0):
                    obj = AttendanceData.objects.create(studentID = student, classScheduleID = q, loginDate = date, loginTime = time)
                    listData.append(obj)
                else:
                    listData.append(check[0])
        else:
            print("cannot do attendant")

        # obj = CoreAttendanceData(data[0], data[1], data[2])

    listData.sort(key = lambda x:x.loginDate,reverse = True)
    # data = AttendanceData.objects.all()

    context = {
        'title' : 'hello',
        'data' : listData
    }

    return render(request, 'attendance/doattendance.html', context)

def submit(request):
    binusianId = request.POST['binusianid']
    name = request.POST['name']

    response = detect(binusianId, name)

    # insert new student data to database
    Student.objects.create(name=name, binusianID = binusianId)

    print("Response : " + str(response))

    return render(request, 'attendance/response.html')


def response(request):
    return render(request, 'attendance/response.html')
