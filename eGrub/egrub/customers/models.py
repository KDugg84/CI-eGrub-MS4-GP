from django.db import models

# Class of menu items for sale
class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name

# Category linked with the ManyToManyField in the category variable in the MenuItems class
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Stores all the order items in variables
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItems', related_name='order', blank=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
