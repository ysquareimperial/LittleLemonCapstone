from django.db import models

class TableBooking(models.Model):
    table_number = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
