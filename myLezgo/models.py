from django.db import models

# Create your models here.
from django.urls import reverse


class Rate(models.Model):
    day = models.IntegerField("Day")
    price = models.IntegerField("Price")


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Car", max_length=150)
    place = models.IntegerField("Place", default=4)
    max_speed = models.IntegerField("MaxSpeed")
    hp = models.IntegerField("HorsePower")
    drive_unit = models.CharField("DriveUnit", default="4wd", max_length=150)
    year = models.IntegerField("Year")
    image = models.ImageField("Image", upload_to='car_images/')
    rate = models.ManyToManyField(Rate, verbose_name="rate")
    slug = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})


class Order(models.Model):
    name = models.CharField("Name", max_length=150)
    surname = models.CharField("Surname", max_length=150)
    number = models.CharField("MobileNumber", max_length=150)
    city = models.CharField("City", max_length=150)
    car = models.ForeignKey(Car, related_name="car", on_delete=models.CASCADE)
    fullFuel = models.BooleanField("FullFuel", default=True)
    water = models.BooleanField("Water", default=False)
    driver = models.BooleanField("Driver", default=False)
    outOfTown = models.BooleanField("TripOutOfTown", default=False)
    sweets = models.BooleanField("Sweets", default=False)
    comments = models.TextField("Comments", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
