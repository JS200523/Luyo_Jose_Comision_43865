from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, UserProfileForm
from .models import UserProfile


def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('home')
    else:
        form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'form': form, 'profile_form': profile_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')


@login_required
def profile_view(request):
    profile = request.user.userprofile
    return render(request, 'profile.html', {'profile': profile})


@login_required
def update_profile_view(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'profile_form': profile_form})