from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.DecimalField(max_digits=6,decimal_places=0)
    booking_date = models.DateField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.DecimalField(max_digits=5,decimal_places=0)
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'    
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'