from django.urls import path, include
from users.views import user_dashboard, user_registration

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', user_registration, name='register')

]