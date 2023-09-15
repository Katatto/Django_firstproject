from django.shortcuts import render, redirect  
from crudprojectapp.forms import StudentForm  
from crudprojectapp.models import Student  
 
# Create your views here.  

# def home(request):
#     return render(request, 'base.html')
 
#  add function
def addnew(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  
 
#  display data in table
def index(request):  
    student = Student.objects.all()  
    return render(request,"show.html",{'student':student})  

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
        return redirect("/")  
    return render(request, 'edit.html', {'student': student})  
     
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/")   