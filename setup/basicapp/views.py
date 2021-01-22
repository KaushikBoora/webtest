from django.shortcuts import render
from basicapp.forms import userForms,userProfileInfo
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def registration(request):
    registered=False
    if request.method=='POST':
        userForm=userForms(data=request.POST)
        userProfile=userProfileInfo(data=request.POST)

        if userForm.is_valid() and userProfile.is_valid():

            user=userForm.save()
            user.set_password(user.password)
            user.save()

            profile=userProfile.save(commit=False)
            profile.user= user
            if 'Picture' in request.FILES:
                profile.Picture=request.FILES['Picture']
            profile.save()
            registered=True
        else:
            print(userForm.errors,userProfile.errors)
    else:
        userForm=userForms()
        userProfile=userProfileInfo()
        print("Entered reg")
    return render(request,'basicapp/registrartion.html',{'uf':userForm,'upi':userProfile,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def user_login(request):
    print("inside user login")
    print(request.method)
    if request.method=="POST":
        print("INSIDE POST")
        username=request.POST.get("em")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                print("active user")
                return HttpResponseRedirect(reverse("index"))
            else :
                print("inactive user")
                print("{} AINT ACTIVE ".format(user.username))
                return HttpResponse("{} AINT ACTIVE ".format(user.username))
        else :
            print("NO user")
            return HttpResponse("{} is not Registered, Please REGISTER".format(username))
    else:
        return render(request,"basicapp/login_page.html",{})
