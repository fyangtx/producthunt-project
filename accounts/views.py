from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #todo: route to homepage and logout
    return render(request, 'acounts/signup.html')