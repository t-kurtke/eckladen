from django.shortcuts import render, redirect
from users.forms import Custom_user_creation_form
from django.urls import reverse
from django.contrib.auth import login

# Create your views here.
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def user_registration(request):
    if request.method == 'GET':
        context = {
            'form': Custom_user_creation_form,
        }
        return render(request, 'register.html', context)
    elif request.method == 'POST':
        form = Custom_user_creation_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))