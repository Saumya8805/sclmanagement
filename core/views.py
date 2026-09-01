from django.shortcuts import render , get_object_or_404 , redirect
from .models import Student, Result , Teacher , Student , ClassRoom , Attendance
from .models import Exam, Result
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


### for home page 
def home(request):
    return render(request, 'home.html')



### to login in the project if you handle both teacher and student pannel have power
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')




### login for teacher and student

@login_required
def dashboard(request):
    user = request.user
    if hasattr(user, 'teacherprofile'):
        # Teacher dashboard
        return render(request, 'teacher_dashboard.html', {'teacher': user.teacherprofile})
    elif hasattr(user, 'studentprofile'):
        # Student dashboard
        return render(request, 'student_dashboard.html', {'student': user.studentprofile})
    else:
        # Admin or generic user
        return render(request, 'admin_dashboard.html')



### push the data  student list

def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html', {'students': students_list})


### push the data into the teacher list
def teachers(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers_list})



#### push the classroom data 
def classes(request):
    classes_list = ClassRoom.objects.all()
    return render(request, 'classes.html', {'classes': classes_list})





### to store attendance of childerns
def attendance(request):
    attendance_list = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance.html', {'attendance': attendance_list})



def exams(request):
    exams_list = Exam.objects.all()
    results_list = Result.objects.all()
    return render(request, 'exams.html', {
        'exams': exams_list,
        'results': results_list
    })




def report_card(request):
    return HttpResponse('Report card section')




