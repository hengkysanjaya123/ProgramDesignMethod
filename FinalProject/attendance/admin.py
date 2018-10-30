from django.contrib import admin


# Register your models here.
from .models import AttendanceData, Student

admin.site.register(Student)
admin.site.register(AttendanceData)
