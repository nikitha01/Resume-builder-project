from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('nik/', admin.site.urls),
    path('login/',views.main, name = "main"),
    path("", views.login, name = "registration"),
    path('add_user/', views.add_user, name="add_user"),
    path('profile/', views.profile, name="profile"),
    path('resume/',views.resume, name="resume")
]


