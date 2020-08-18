from django.urls import path
from tauschboerse import views

urlpatterns = [
    path("create/", views.GegenstandCreate.as_view(), name="gegenstand_create"),
    path("<int:pk>/", views.gegenstand_detail, name="gegenstand_detail"),
    path("<int:pk>/update/", views.GegenstandUpdate.as_view(), name="gegenstand_update"),
    path("<int:pk>/delete/", views.GegenstandDelete.as_view(), name="gegenstand_delete"),
    #path("create/", views.gegenstand_create, name="gegenstand_create"),
    path("", views.gegenstaende_index, name="tauschboerse"),
    path("<user_name>/", views.gegenstaende_user, name="gegenstaende_user"),

    ]
