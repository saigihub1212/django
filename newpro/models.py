from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class  createCourse(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=(
            ("student","Student"),
            ("teacher","Teacher"),
            ("admin","Admin")
        )
    )

    def  __str__(self):
        return f"{self.user.username} - {self.role}"
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    joined_date=models.DateField(auto_now_add=True)
class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
class Course(models.Model):
    title = models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    students=models.ManyToManyField(Student)
class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    score =models.IntegerField()