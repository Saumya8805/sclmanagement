from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),   # root path
    path('rep/', views.report_card, name='report_card'),
    path('login/', views.user_login, name='login'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('classes/', views.classes, name='classes'),
    path('attendance/', views.attendance, name='attendance'),
    path('exams/', views.exams, name='exams'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('student-register/', views.student_register, name='student_register'),
    path('teacher-register/', views.teacher_register, name='teacher_register'),
    path('student-profile/', views.student_profile, name='student_profile'),
    path('teacher-profile/', views.teacher_profile, name='teacher_profile'),
    



]
