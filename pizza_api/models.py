from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Create your models here.
class User(AbstractUser):
    user_type_data=(("Managet","Manager"),("Staff","Staff"),("Customer","Customer"))
    user_type=models.CharField(choices=user_type_data,max_length=10)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.user_type = "Manager"
        elif self.is_staff:
            self.user_type = "Staff"
        else:
            self.user_type = "Customer"
        super(User, self).save(*args, **kwargs)


class Topping(models.Model):
    name = models.CharField(max_length=60)
    toppingprice = models.IntegerField()
    discription = models.TextField()

    def __str__(self):
        return str(self.name)

class Price(models.Model):
    price = models.IntegerField(default=100)

    def __str__(self):
        return str(self.price)


class Pizza(models.Model):
    topping = models.ForeignKey(Topping, on_delete=DO_NOTHING)
    price = models.IntegerField(default=Price)

    def save(self, *args, **kwargs):
        a = Topping.objects.get(name=self.topping)
        b = a.toppingprice
        self.price = self.price + b
        return super(Pizza, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.topping)+"["+str(self.price)+']'


class Order(models.Model):
    pizza_type = (('Regular','Regular'), ('Square','Square'))
    pizza_size = (('Small','Small'), ('Medium','Medium'), ('Large','Large'))
    order_id = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Topping, on_delete=DO_NOTHING)
    type = models.CharField(choices=pizza_type, max_length=50)
    size = models.CharField(choices=pizza_size, max_length=50)
    price = models.IntegerField(default=Price)
    customer_name = models.CharField(max_length=50)
    customer_address = models.TextField()

    def save(self, *args, **kwargs):
        if self.size == 'Large':
            self.price = self.price*2
        if self.size == 'Medium':
            self.price = self.price + self.price/2

        a = Topping.objects.get(name=self.pizza)
        b = a.toppingprice
        self.price = self.price + b
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.type)+'-'+str(self.pizza)+"["+str(self.order_id)+']'

