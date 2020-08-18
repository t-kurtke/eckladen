from django.urls import path, include
from users.views import user_dashboard, user_delete

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/profile', user_dashboard, name='user_dashboard'),
    path('accounts/delete', user_delete, name='user_delete')
]
