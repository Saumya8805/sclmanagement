from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#### STUDENT MODEL 

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    dob = models.DateField()
    email = models.EmailField()
    class_name = models.CharField(max_length=50)
  

    def __str__(self):
        return f"{self.name} ({self.roll_no})"






## TEACHER MODEL
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


### CLASROOM MODEL

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)   # Example: "10th Grade A"
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name


#######ATTENDANCE MODEL SO THAT WE CAN MAINTAIN THE ATTENDANCE

class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date} ({self.status})"


#### FOR THE EXAMS

class Exam(models.Model):
    name = models.CharField(max_length=100)   # Example: "Mid Term 2026"
    date = models.DateField()
    class_room = models.ForeignKey('ClassRoom', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.class_room.name}"


#V FOR THE REs

class Result(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.exam.name} ({self.subject}: {self.marks})"




## creae  a different pannel for both and teacher so that both caan use smoothly

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username





class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)
    student_class = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username


