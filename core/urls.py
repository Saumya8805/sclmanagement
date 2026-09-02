from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),   # root path

    path('login/', views.user_login, name='login'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('classes/', views.classes, name='classes'),
    path('attendance/', views.attendance, name='attendance'),
    path('exams/', views.exams, name='exams'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('report/<int:student_id>/', views.report_card, name='report_card'),







]
