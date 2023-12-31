from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")

    return render(request,"login.html")
def register(request):

    if request.method== 'POST':  #for fetching
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1: #password verification
            if User.objects.filter(username=username).exists(): #checking the name and email is already existiong or not
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"E-mail Taken")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                 user.save();
                 print("User registed")
                 return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return  redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')