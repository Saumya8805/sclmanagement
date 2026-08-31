from django.contrib import admin

from .models import Student
from .models import Teacher
from .models import ClassRoom
from .models import Attendance
from .models import Exam, Result



# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ClassRoom)
admin.site.register(Attendance)
admin.site.register(Exam)
admin.site.register(Result)
