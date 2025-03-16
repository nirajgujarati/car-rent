from django.urls import path
from .views import register, login_view, logout, user_dashboard, car_owner_dashboard,add_car,list_cars

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("user/dashboard/", user_dashboard, name="user_dashboard"),
    path("owner/dashboard/", car_owner_dashboard, name="car_owner_dashboard"),
    path("logout/", logout, name="logout"),
    path("add_car/", add_car, name="add_car"),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)