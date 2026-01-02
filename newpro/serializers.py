from rest_framework import serializers
from .models import Student, Teacher , Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'joined_date']
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields=['id','name','department']
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=['id','title','teacher','students']
