from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User,Car
import hashlib

from django.shortcuts import render 
from django.contrib.auth.hashers import check_password

from django.contrib.sessions.models import Session
from .models import User, CarOwner
import hashlib

def register(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        emergency_contact = request.POST['emergency_contact']
        dob = request.POST['dob']
        driving_license = request.POST['driving_license']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        password = request.POST['password']  # Store directly, no hashing

        # Store data in the database
        user = User.objects.create(
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            emergency_contact=emergency_contact,
            dob=dob,
            driving_license=driving_license,
            gender=gender,
            address=address,
            city=city,
            state=state,
            country=country,
            password=password  # Directly storing
        )

        print(f"✅ User {user.email} registered successfully with plain text password")
        return redirect("login")

    return render(request, "register.html")




from django.shortcuts import render, redirect
from .models import User, CarOwner

def login_view(request):
    if request.method == "POST":
        email_or_username = request.POST.get("email")  # Get email/username
        password = request.POST.get("password")  # Get password

        if not email_or_username or not password:
            return render(request, "login.html", {"error": "Email/Username and Password are required"})

        # Check if it's a User (email login)
        user = User.objects.filter(email=email_or_username).first()
        if user:
            print(f"🔍 Found user: {user.email}")  # Debugging
            if password == user.password:  # Directly compare passwords
                request.session["user_id"] = user.id
                print(f"✅ User {user.email} logged in. Redirecting to user dashboard...")
                return redirect("user_dashboard")
            else:
                print("❌ Incorrect password for user")
                return render(request, "login.html", {"error": "Invalid password"})

        # Check if it's a Car Owner (username login)
        car_owner = CarOwner.objects.filter(username=email_or_username).first()
        if car_owner:
            print(f"🔍 Found car owner: {car_owner.username}")  # Debugging
            if password == car_owner.password:  # Directly compare passwords
                request.session["car_owner_id"] = car_owner.id
                print(f"✅ Car Owner {car_owner.username} logged in. Redirecting to car owner dashboard...")
                return redirect("car_owner_dashboard")
            else:
                print("❌ Incorrect password for car owner")
                return render(request, "login.html", {"error": "Invalid password"})

        # If no user found
        print("❌ Invalid login attempt: No user found")
        return render(request, "login.html", {"error": "Invalid email/username or password"})

    return render(request, "login.html")







def logout(request):
    request.session.flush()
    return redirect("login")


def user_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect("login")

    user = User.objects.get(id=user_id)
    
    available_cars = Car.objects.filter(status="Available")  # Fetch available cars
    
    return render(request, "user_dashboard.html", {"user": user, "cars": available_cars})
    # return render(request, "user_dashboard.html", {"user": user})


def car_owner_dashboard(request):
    car_owner_id = request.session.get('car_owner_id')
    if not car_owner_id:
        return redirect("login")

    car_owner = CarOwner.objects.get(id=car_owner_id)
    owner_cars = Car.objects.filter(owner=car_owner)  # Fetch cars owned by the logged-in car owner
    
    return render(request, "owner_dashboard.html", {"car_owner": car_owner, "owner_cars": owner_cars})

