from django.shortcuts import redirect, render
from .models import Git


# Create your views here.
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
