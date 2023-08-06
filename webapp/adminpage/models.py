from django.db import models

# Create your models here.
class Customers(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)


    def __str__(self):

        return self.user_name,self.email