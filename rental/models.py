from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    emergency_contact = models.CharField(max_length=15)
    dob = models.DateField()
    driving_license = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  # Hashed manually
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class CarOwner(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # Hashed manually
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Car(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)  # Each car belongs to a car owner
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20, unique=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)
    with_driver = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.number_plate}"