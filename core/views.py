from django.shortcuts import render , get_object_or_404 , redirect
from .models import Student, Result
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')





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


def students(request):
    return HttpResponse("Students Section")

def teachers(request):
    return HttpResponse("Teachers Section")

def classes(request):
    return HttpResponse("Classes Section")

def attendance(request):
    return HttpResponse("Attendance Section")

def exams(request):
    return HttpResponse("Exams & Results Section")

def report_card(request):
    return HttpResponse('Report card section')




