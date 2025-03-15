from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password from API response
        }

    def create(self, validated_data):
        validated_data['password'] = User.objects.make_random_password()  # Ensure password is hashed
        return super().create(validated_data)
