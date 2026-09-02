from django.shortcuts import render , get_object_or_404 , redirect
from .models import Student, Result , Teacher , Student , ClassRoom , Attendance
from .models import Exam, Result
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import StudentProfile, TeacherProfile, ClassRoom
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.db.models import Q
from django.contrib.auth.models import User




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

@login_required
def classes(request):
    user = request.user
    if hasattr(user, 'teacherprofile'):
        # Teacher sees only their classes
        classes_list = ClassRoom.objects.filter(teacher=user.teacherprofile)
    else:
        # Admin sees all classes
        classes_list = ClassRoom.objects.all()
    return render(request, 'classes.html', {'classes': classes_list})


### to store attendance of childerns
@login_required
def attendance(request):
    user = request.user
    if hasattr(user, 'studentprofile'):
        # Student sees only their own attendance
        attendance_list = Attendance.objects.filter(student=user.studentprofile)
    elif hasattr(user, 'teacherprofile'):
        # Teacher sees attendance for their classes
        attendance_list = Attendance.objects.filter(student__class_room__teacher=user.teacherprofile)
    else:
        # Admin sees all
        attendance_list = Attendance.objects.all()
    return render(request, 'attendance.html', {'attendance': attendance_list})



# to store the exams information
def exams(request):
    exams_list = Exam.objects.all()
    results_list = Result.objects.all()
    return render(request, 'exams.html', {
        'exams': exams_list,
        'results': results_list
    })


# user can logout through this

def user_logout(request):
    logout(request)
    return redirect('login')


# To  show the result of students
@login_required
def report_card(request, student_id):
    user = request.user
    student = get_object_or_404(Student, id=student_id)

    # Restrict: student can only view their own report
    if hasattr(user, 'studentprofile') and student.id != user.studentprofile.id:
        return HttpResponse("Unauthorized", status=403)

    results = Result.objects.filter(student=student)
    return render(request, 'report_card.html', {
        'student': student,
        'results': results
    })


# for search
def search(request):
    query = request.GET.get('q')
    students = teachers = None
    if query:
        students = StudentProfile.objects.filter(
            Q(user__username__icontains=query) | Q(roll_no__icontains=query)
        )
        teachers = TeacherProfile.objects.filter(
            Q(user__username__icontains=query) | Q(subject__icontains=query)
        )
    return render(request, 'search_results.html', {
        'query': query,
        'students': students,
        'teachers': teachers
    })






