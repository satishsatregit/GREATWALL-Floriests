from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=25)

    def __str__(self):
        return self.category_name
    class Meta:
        db_table="Category"

class Product(models.Model):
    pname=models.CharField(max_length=20)
    price=models.FloatField(default=200)
    description=models.CharField(max_length=50)
    quantity=models.IntegerField()
    image=models.ImageField(default='simple handtied.jpg',upload_to='temp')
    cat=models.ForeignKey(to='Category',on_delete=models.CASCADE)

    class Meta:
        db_table='Product'

class UserInfo(models.Model):
    uname = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length = 100)
    location = models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"

class PaymentMaster(models.Model):
    cardno = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=20)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "PaymentMaster"
