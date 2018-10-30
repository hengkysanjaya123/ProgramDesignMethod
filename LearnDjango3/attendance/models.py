from django.db import models

# Create your models here.



class Student(models.Model):
    binusianId = models.TextField()
    name = models.TextField()
    # images = models.ForeignKey(StudentImageDetails, on_delete=models.CASCADE, null=True)


class StudentImageDetails(models.Model):
    binusianId = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dataset', null=False)
