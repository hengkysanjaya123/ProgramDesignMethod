from django.shortcuts import render
from .models import AttendanceData, Student
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.files import File
from .core import CoreAttendanceData
from django.http import HttpResponse



from .detectface import detect

# Create your views here.
def home(request):
    return render(request, 'attendance/homepage.html')

def traindata(request):
    return render(request, 'attendance/traindata.html')


def doattendance(request):
    url = 'attendance/temporarydata.txt'

    f = open(url, 'r')

    listData = []
    for i in f:
        data = i.split('#')
        obj = CoreAttendanceData(data[0], data[1], data[2])
        listData.append(obj)

    listData.sort(key = lambda x:x.login,reverse = True)
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

    print("Response : " + str(response))

    return render(request, 'attendance/response.html')


def response(request):
    return render(request, 'attendance/response.html')
