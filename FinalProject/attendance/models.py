from django.db import models

# Create your models here.

class Student(models.Model):
    binusianID = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.binusianID + " ( "+ self.name +" )"

    def getBinusianID(self):
        return self.binusianID

    def getName(self):
        return self.name

class AttendanceData(models.Model):
    binusianID = models.ForeignKey(Student, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __init__(self, binusianID, datetime):
        self.binusianID = binusianID
        self.datetime = datetime

    def __str__(self):
        return str(self.binusianID) + " (  "+ str(self.datetime) +"  )"

    def getStudent(self):
        return self.binusianID

    def getDateTime(self):
        return self.datetime

