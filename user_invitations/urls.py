from django.urls import path, include

urlpatterns=[
    path('invitations/', include('invitations.urls', namespace='invitations')),
]
