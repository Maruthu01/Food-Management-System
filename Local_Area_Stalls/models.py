from django.db import models
from django.contrib.auth.models import User


class IcecreamStall(models.Model):
        Name = models.CharField(max_length=100)
        Ice_type = models.CharField(max_length=100)
        Contact_num = models.CharField(max_length=100)
        Address = models.CharField(max_length=100)
        opening_time = models.CharField(max_length=100)
        closing_time = models.CharField(max_length=100)
        Stall_images = models.ImageField(upload_to='stall_images/')
        Location = models.URLField(max_length=500,default='NIL')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.Name   


class JuiceStall(models.Model):
        Name = models.CharField(max_length=100)
        Juice_type = models.CharField(max_length=100)
        Contact_num = models.CharField(max_length=100)
        Address = models.CharField(max_length=100)
        opening_time = models.CharField(max_length=100)
        closing_time = models.CharField(max_length=100)
        Stall_images = models.ImageField(upload_to='stall_images/')
        Location = models.URLField(max_length=500,default='NIL')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.Name



class FoodStall(models.Model):
        Name = models.CharField(max_length=100)
        Food_type = models.CharField(max_length=100)
        Contact_num = models.CharField(max_length=100)
        Address = models.CharField(max_length=100)
        ratings = models.FloatField(max_length=100)
        opening_time = models.CharField(max_length=100)
        closing_time = models.CharField(max_length=100)
        Stall_images = models.ImageField(upload_to='stall_images/')
        Location = models.URLField(max_length=500,default='NIL')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.Name    


class Register(models.Model):
    User_name =models.CharField(max_length=100)
    Email_id = models.EmailField()
    Ph_no = models.CharField(max_length=15)
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.User_name