from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .services.authServices import AuthServices

# Create your views here.
def login_view(request):
    title = "Login"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = AuthServices.login(request, username, password)
            return redirect('dashboard')
    return render(request, 'auth/login.html', {'title': title})

        
def logout(request):
    if request.method == 'POST':
        AuthServices.logout(request)
        return redirect('login')
        
        