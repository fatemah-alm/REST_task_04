from rest_framework import serializers

from .models import Flight, Booking
from django.contrib.auth import get_user_model
User = get_user_model()


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']
  
  
  
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password', 'first_name', 'last_name']
        
    def create(self, user_data):
        username = user_data['username']
        password = user_data['password']
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        newUser = User(username=username, first_name=first_name, last_name=last_name)
        newUser.set_password(password)
        newUser.save()
        return user_data
        
    
    
        

