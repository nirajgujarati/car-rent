from django.urls import path
from .views import register, login_view, logout, user_dashboard, car_owner_dashboard,add_car,list_cars,remove_car,view_available_cars,book_car

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("user/dashboard/", user_dashboard, name="user_dashboard"),
    path("owner/dashboard/", car_owner_dashboard, name="car_owner_dashboard"),
    path("logout/", logout, name="logout"),
    path("add_car/", add_car, name="add_car"),
    path('remove_car/<int:car_id>/', remove_car, name='remove_car'),
]
