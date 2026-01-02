# from django.shortcuts import render
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# from .models import Student,Course,Teacher,Marks

# def get_students(request):
#     students = Student.objects.all()

#     data =[]
#     for s in students:
#         data.append({
#             "id": s.id,
#             "name":s.name,
#             "email":s.email
#         })
#     return JsonResponse(data, safe=False)
# def get_student_id(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     data = {
#         "id": student.id,
#         "name":student.name,
#         "email":student.email
#     }
#     return JsonResponse(data)
# def get_course(request):
#     course = Course.objects.all()
#     data_1=[]
#     for i in course:
#         data_1.append({
#             "title": i.title,
#             "teacher": i.teacher.name,
#             # "students": i.students
#         }
#         )
#     return JsonResponse(data_1,safe=False)

# @csrf_exempt
# def create_student(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Method not allowed"},status=405)
#     try:
#         data = json.loads(request.body)
#     except json.JSONDecoderError:
#         return JsonResponse({"error":"Invalid Json"},status=400)
#     if not data.get("name") or not data.get("email"):
#         return JsonResponse({
#             "error":"name and email are required"
#         },)
#     student= Student.objects.create(
#         name=data["name"],
#         email=data["email"],
#         # joined_data=data.get("joined_data")
#     )
#     return JsonResponse({
#         "message":"Student done",
#         "id": student.id
#     },status=201)

# #put
# @csrf_exempt
# def update_student(req,student_id):
#     if req.method != "PUT":
#         return JsonResponse({"error":"method not allowed"},status=405)
#     student = get_object_or_404(Student,id=student_id)

#     try:
#         data=json.loads(req.body)
#     except json.JSONDecoderError:
#         return JsonResponse({"error":"Invalid"},status=400)
#     student.name = data.get("name",student.name)
#     student.email= data.get("email",student.email)
#     student.save()
#     return JsonResponse({
#         "message":"student Updated"
#     },status=200)
# #Delete 
# @csrf_exempt
# def delete_id(req,student_id):
#     if req.method != "DELETE":
#         return JsonResponse({"error":"method not allowed"},status=405)
#     student = get_object_or_404(Student,id=student_id)
#     student.delete()
#     return JsonResponse({
#         "message":"ayypoindhi"
        
#     },status=200)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student,Teacher,Course
from .serializers import StudentSerializer,TeacherSerializer,CourseSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin,IsTeacher,IsStudent
class CreateCourseAPI(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def post(self,req):
        title = req.data.get('title')
        course = Coursre.objects.create(
            title=title,
            teacher=None
        )
        return Response({
            "message":"Course created done",
            "course_id": course.id
        })
class StudentListCreate(APIView):
    def get(self,req):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    def post(self,req):
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,req,student_id):
        try:
            student=Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(student,data=req.data,  partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,req,student_id):
            student=Student.objects.get(id=student_id)
        # serializer=StudentSerializer(student)
        # if student.is_valid():
            student.delete()
            return Response({"message":"deleted"})
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
### this is for Teacher

class TeacherListCreate(APIView):
    def get(self,req):
        teacher=Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    def post(self,req):
        serializer=TeacherSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,req,teacher_id):
        try:
            teacher=Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"error":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer=TeacherSerializer(teacher,data=req.data,  partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,req,teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except:
            return Response({"error":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        return Response({"message":"done bro"})
### this is for course
class CourseListCreate(APIView):
   def get(self,req):
      course=Course.objects.all()
      serializer = CourseSerializer(course,many=True)
      return Response(serializer.data)
   def post(self,req):
       serializer=CourseSerializer(data=req.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   def put(self,req,course_id):
        try:
            course=Course.objects.get(id=course_id)
        except Course.DoesNotExist:
             return Response({"error":"Student Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer=CourseSerializer(course,data=req.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   def delete(self,req,course_id):
        try:
            course=Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"message":"Not such Course"},status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response({"message":"katham"})
         