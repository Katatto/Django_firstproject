from django.shortcuts import render, redirect  
from crudprojectapp.forms import StudentForm  
from crudprojectapp.models import Student  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.  


def landinpage(request):
     return render(request, 'register.html', {})

@login_required 
def HomePage(request):  
    student = Student.objects.all()  
    return render(request,"show.html",{'student':student})  


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('home-page')
    
    return render(request, 'register.html', {})


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return render(request, 'register.html', {'error_message': 'Invalid credentials'})

    return render(request, 'register.html', {})

def logoutuser(request):
    logout(request)
    return redirect('/')


#  add function
def addnew(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('home-page')  
            except:  
                pass
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  
 

# Edit function
def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  

# update function 
def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("home-page")  
    return render(request, 'edit.html', {'student': student})  
     
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("home-page")   
