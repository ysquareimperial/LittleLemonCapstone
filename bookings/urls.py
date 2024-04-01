from django.urls import path
from .views import TableBookingList, TableBookingDetail

urlpatterns = [
    path('bookings/', TableBookingList.as_view()),
    path('bookings/<int:pk>/', TableBookingDetail.as_view()),
]
