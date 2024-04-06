from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=25, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone}'


class Products(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.count}'


class Orders(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} заказал {self.products}'
