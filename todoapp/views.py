from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    tasks=Task.objects.all()
    
    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'home.html',{'tasks':tasks,'form':form})

def updatetask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'update_task.html',{'form':form})

def deleteTask(request,pk):
    tasks=Task.objects.get(id=pk)

    if request.method=='POST':
        tasks.delete()
        return redirect('home')

    return render(request,'delete.html',{'task':tasks})

def loginPage(request):
    
    page="login"
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            user=User.objects.get(username=username)
        except:
            print("Username Not Found")
    
        user=authenticate(request,username=username,password=password)

        if user is not None :
            login(request,user)
            return redirect("home")
        
        else:
            print("Username or Password Not found")

    return render(request,'login_register.html',{'page':page})

def registerPage(request):

    page="Register"
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("home")
    
    return render(request,'login_register.html',{"form":form,"page":page})

def logoutPage(request):
    logout(request)
    return redirect("home")