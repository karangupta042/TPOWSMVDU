from django.shortcuts import render,redirect
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'resume' in request.FILES: 
                profile.resume = request.FILES['resume']
            profile.save()
            auth.login(request, user)
            return redirect('home')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'accounts/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')