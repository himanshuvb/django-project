from django.shortcuts import get_object_or_404, redirect, render
from .models import Git, Student
from django.contrib.auth.decorators import login_required
from django.core.files import File


# Create your views here.
@login_required
def index(request):
    if request.method == "GET":
        return render(request, "SMS/index.html")
     
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        new_git = Git()
        new_git.name = name
        new_git.email = email
        new_git.message = message
        new_git.save()

    return redirect('index')


@login_required
def student_list(request):
    student_list = Student.objects.all()
    return render(request, "SMS/student_details.html", context={"all_students": student_list})

@login_required
def add_student(request, student_id):
    if request.method == "GET":
        student = get_object_or_404(Student, id=student_id, user=request.user)
        return render(request, "SMS/add_student.html", context={'album': student})
    if request.method == "POST":
        student = get_object_or_404(Student, id=student_id)
        name = request.POST['student_name']
        roll = request.POST['student_roll']
        regno = request.POST['student_regno']
        age = request.POST['student_age']
        div = request.POST['student_div']
        profile = File(request.FILES.get('profile'))
        

        new_stu = Student()
        new_stu.name = name
        new_stu.roll = roll
        new_stu.regno = regno
        new_stu.age = age
        new_stu.div = div
        new_stu.profile = profile
        new_stu.save()

        return redirect('student_details', student.id)