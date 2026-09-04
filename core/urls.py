from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),   # root path

# for the student information
    path('students/', views.students, name='students'),

# for the teacher information
    path('teachers/', views.teachers, name='teachers'),

    # for the classes information
    path('classes/', views.classes, name='classes'),


# for the student attendance information
    path('attendance/', views.attendance, name='attendance'), 

    #for the exam information
    path('exams/', views.exams, name='exams'), 

    #for the exam information
    path('logout/', views.user_logout, name='logout'),

    #for the library
    path('library/', views.library, name='library'),

    #for the studennt register
    path('student-register/', views.student_register, name='student_register'),
    #fro the student profile
    path('student-profile/', views.student_profile, name='student_profile'),
    #or the student reportcard

    path('report/<int:student_id>/', views.report_card, name='report_card'),


     
     path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    path('teacher-register/', views.teacher_register, name='teacher_register'),



    path('dashboard/', views.dashboard, name='dashboard'),



    path('login/', views.user_login, name='login'),



    







]
