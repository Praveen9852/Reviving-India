from django.urls import path
from . import views
urlpatterns = [
    path("Signup/", views.CustomerSignup.as_view()),
    path("Login/", views.Customerlogin.as_view()),
]