from django.shortcuts import render
from reg_pro_app.forms import *
from reg_pro_app.models import *

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    return render(request,'reg_pro_app/index.html')

def register(request):

    registeredvar=False

    if request.method == "POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registeredvar=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'reg_pro_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registeredvar':registeredvar})


@login_required
def logoutfunc(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in nice!!")

def loginfunc(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tries to login and failed")
            print("Username :{} and password {}.format(username,password)")
            return HttpResponse("innvalid login details supplied")
    else:
        return render(request,'reg_pro_app/login.html')
