from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

# View to take user to the login page
def user_login(request):
    return render(request, 'authentication/login.html')

# View to authenticate user
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    # Check if the user doesn't exist
    if user is None:
        # Send the user back to login
        return HttpResponseRedirect(reverse('user_auth:login'))
    
    else: # If user exists, login user and 
        # take user to a new page showing their details
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
    

# This view reads in the user data and sends it to a new HTML file
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

