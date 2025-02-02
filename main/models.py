from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __iter__(self):
        products = self.products.filter(is_visible=True)
        for product in products:
            yield product

    class Meta:
        ordering = ('sort', 'name')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/products/")
    price = models.DecimalField(max_digits=7, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/gallery/")
    is_visible = models.BooleanField(default=True)

    sort = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="slug")
    short_desc = models.TextField(max_length=500, blank=True)
    desc = models.TextField(max_length=2000, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to="images/events/", blank=True)
    date_time = models.DateTimeField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)
    sort = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "events"
        ordering = ('date_time',)
        unique_together = ['id', 'slug']


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city_address = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    opening_hours = RichTextField()

    instagram_link = models.CharField(max_length=50)




class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$', message='Невірний номер телефону')


    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, validators=[phone_regex])
    count = models.PositiveSmallIntegerField(default=1)
    message = models.TextField(blank=True)

    is_confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'

    class Meta:
        ordering = ('-created_at',)









