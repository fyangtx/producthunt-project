from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # user entered info and wants to an account setup.
        if request.POST['password1'] == request.POST['password2']:
            try:
                # check existing user name.               
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already been taken!!!'})            
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')        
            
    else:
        # user wants to enter info.
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #todo: route to homepage and logout
    return render(request, 'acounts/signup.html')