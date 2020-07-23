from django.urls import path
from . import views

urlpatterns = [
    path("", views.gegenstaende_index, name="gegenstaende_index"),
    path("<int:gegenstand_pk>/", views.gegenstand_detail, name="gegenstand_detail"),
    ]
