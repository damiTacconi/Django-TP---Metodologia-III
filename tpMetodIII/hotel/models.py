from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Host(User):
    class Meta:
        verbose_name_plural='Hosts'

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Name: %s" % self.name

class Ownership(models.Model):
    amount_pax = models.IntegerField(default=1)
    title = models.CharField(max_length=60, default='Undefined Title')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    cover = models.ImageField(blank=False, null=False, upload_to='static/images/', default='')
    rate = models.FloatField(default=0)
    host = models.ForeignKey(Host,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "\nCity: \t %s" % self.city
class Book(models.Model):
    book_number = models.IntegerField(blank=False,default=0)
    date = models.DateTimeField(blank=True, default=None)
    client_name = models.CharField(blank=False , max_length=30, default=None)
    client_email = models.CharField(blank=False, max_length=60, default=None)

    def __str__(self):
        return "\nBookNumber: %s" % self.book_number

class RentalDate(models.Model):
    date = models.DateTimeField()
    ownership = models.ForeignKey(Ownership, on_delete=models.CASCADE,default=None)
    booked = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "\nDate:  %s , \nBooked: \t %s \nOwnership: \t %s" % (self.date, self.booked, self.ownership)