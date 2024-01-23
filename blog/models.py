from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Manclothes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='Manclothes/img')
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wclothes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='Wclothes/img')
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.TextField()
    img = models.ImageField(upload_to='Banner/img')
    img2 = models.ImageField(upload_to='Banner/img')

    def __str__(self):
        return self.name

class Devices(models.Model):
    name = models.CharField(max_length=100)
    oldprice = models.IntegerField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='Devices/img')
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Laptops(models.Model):
    name = models.CharField(max_length=100)
    oldprice = models.IntegerField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='Laptops/img')
    brand = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse("laptopDetail", args=[self.slug])

    def __str__(self):
        return self.name


class Mbanner(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Mbanner/img')

    def __str__(self):
        return self.name

class Wbanner(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Wbanner/img')

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Aboutus(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Aboutus/img')

    def __str__(self):
        return self.name