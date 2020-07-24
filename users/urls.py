from django.urls import path, include
from users.views import user_dashboard, user_registration

urlpatterns = [
    path('accounts/profile', user_dashboard, name='user_dashboard'),
]
