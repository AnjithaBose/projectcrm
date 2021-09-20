from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        user=request.user
        if user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'common/login.html')

    def post(self,request):
        username= request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            msg="Invalid Login Credentials.Try again!.."
            return render(request,'common/login.html',{'msg':msg})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class HomeView(View):
    def get(self,request):
        user=request.user
        if user.is_authenticated:
            try:
                s = Staff.objects.get(user=user)
                if s.staff_type == 'Operations' :
                    return HttpResponse('Operations')
                elif s.staff_type == 'Sales' :
                    return HttpResponse('Sales')
                elif s.staff_type == 'Trainer' :
                    return HttpResponse('Trainer')
                elif s.staff_type == 'Admin' : 
                    return HttpResponse('Admin')
            except:
                return HttpResponse("Student")
        else:
            return redirect('logout')
