from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from users.forms import SignupProfileForm, UserDeleteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

@login_required
def user_delete(request):
    if request.method == 'GET':
        return render(request, 'user_delete.html', {'form': UserDeleteForm})
    elif request.method == 'POST':
        request.user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('blog_index')

# def user_edit_contact(request):
#     if request.method == 'GET':
#         return render(request, 'user_edit_contact.html', {'form': UserEditContactForm})
#     elif request.method == 'POST':
#         request.user.profile.contact
#         return redirect('blog_index')