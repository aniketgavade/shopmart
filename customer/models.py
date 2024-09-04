from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.
class Cart(models.Model):
   customer_id=models.ForeignKey(User, on_delete=models.CASCADE,db_column="customer_id")
   product_id=models.ForeignKey(Product, on_delete=models.CASCADE,db_column="product_id")


#    db_column==database column name
   quantity=models.IntegerField()

class Profile(models.Model):
   user_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
   contact=models.CharField( max_length=50)
   street=models.CharField( max_length=50)   
   city=models.CharField( max_length=50)
   state=models.CharField( max_length=50)
   pincode=models.CharField( max_length=50)