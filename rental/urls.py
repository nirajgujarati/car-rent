from django.urls import path
from .views import register, login_view, logout, user_dashboard, car_owner_dashboard

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("user/dashboard/", user_dashboard, name="user_dashboard"),
    path("owner/dashboard/", car_owner_dashboard, name="car_owner_dashboard"),
    path("logout/", logout, name="logout"),
    
]
