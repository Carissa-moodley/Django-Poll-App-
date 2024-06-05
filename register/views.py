from django.shortcuts import render, redirect
from django.contrib.auth import logout 
from . forms import RegisterForm

# Create your views here.
# View that allows a new user to register
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form':form})

# View that allows user to logout 
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')
