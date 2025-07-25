from django.shortcuts import render
from urllib3 import request
from .utils import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .utils import fetch_and_save_data
from django.shortcuts import redirect

@login_required
def contest_history(request):
    fetch_and_save_data(request.user) 
    user_profile = request.user.userprofile
    cf_handle = user_profile.codeforces_handle
    lc_handle = user_profile.leetcode_handle

    cf_contest_data = CodeforcesContest.objects.filter(handle=cf_handle).order_by('-timestamp')
    lc_contest_data = LeetcodeContest.objects.filter(handle=lc_handle)

    
    return render(request, 'contest_history.html', {'cf_contests': cf_contest_data,'lc_contests': lc_contest_data.first(),'user_profile': user_profile})

from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def update_handles(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('contest_history')  
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'update_handles.html', {'form': form})

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            codeforces_handle = form.cleaned_data['codeforces_handle']
            leetcode_handle = form.cleaned_data['leetcode_handle']
            

            user = User.objects.create_user(username=username, password=password)

            # Signal will auto-create UserProfile
            user.userprofile.codeforces_handle = codeforces_handle
            user.userprofile.leetcode_handle = leetcode_handle
            
            user.userprofile.save()

            login(request, user)
            return redirect('contest_history')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})




def home(request):
    return render(request, 'home.html')

