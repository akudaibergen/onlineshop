from django.db import models
from django.conf import settings
from _datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}: {}'.format(self.id,
                               self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    image = models.CharField(max_length=200, default="https://sneakertown.kz/bitrix/templates/styleshop_club/components/bitrix/catalog.top/catalog/images/no_photo.png")
    color = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, default='no left sizes')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.name,
                               self.description)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'color': self.color,
            'size': self.size
        }


# class Orders(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True, null=True, blank=True)
#     # status = models.TextField(max_length=50, default='')
#     price = models.IntegerField(Product.price, default=0)

class Order(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    status = models.TextField(max_length=50, default='неплачено')
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    products = models.ManyToManyField(Product)

    def get_products(self):
        return "/n".join([p.products for p in self.products.all()])





