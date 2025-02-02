from django.urls import path
from .views import booking_data, booking_confirm


app_name = 'manager'

urlpatterns = [
    path('booking/', booking_data, name='booking'),
    path('booking/<int:pk>/', booking_confirm, name='booking_confirm'),
]