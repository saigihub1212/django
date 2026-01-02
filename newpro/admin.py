from django.contrib import admin
from .models import Student,Course,Teacher,Marks
# from .models import Course
# from .models import Teacher
# from .models import Marks
# from .models import Item
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Marks)
# Register your models here.
