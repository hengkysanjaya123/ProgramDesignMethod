from django.contrib import admin

# Register your models here.
from .models import Student, StudentImageDetails

admin.site.register(StudentImageDetails)
admin.site.register(Student)

