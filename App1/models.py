from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

# # Create your models here.
class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.IntegerField()
    income_group = models.IntegerField()
    sensing= models.FloatField()
    introvert= models.FloatField()
    Judging= models.FloatField()
    Thinking= models.FloatField()
    logical_intelligence= models.FloatField()
    Nature_intelligence= models.FloatField()
    Visual_intelligence= models.FloatField()
    Musical_intelligence= models.FloatField()
    Body_intelligence= models.FloatField()
    Interpersonal_intelligence= models.FloatField()
    Intrapersonal_intelligence= models.FloatField()
    Verbal_intelligence= models.FloatField()
    Existential_intelligence= models.FloatField()
    Engineering_Field1=models.CharField(max_length=200)
    Engineering_Field2=models.CharField(max_length=200)
    Engineering_Field3=models.CharField(max_length=200)
    Engineering_Field4=models.CharField(max_length=200)
    Engineering_Field5=models.CharField(max_length=200)
    Medical_Field1=models.CharField(max_length=200)
    Medical_Field2=models.CharField(max_length=200)
    Medical_Field3=models.CharField(max_length=200)
    #score = models.FloatField()

    def __str__(self):
        return f"Score: {self.score}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.TextField(max_length=500, blank=True)
    country = models.TextField(max_length=500, blank=True)
    # Add more fields as needed
    # Add any additional methods or properties if required

    def __str__(self):
        return self.user.username


# from django.contrib.auth.models import AbstractUser
# from django.db import models

#Today##
# class CustomUser(AbstractUser):
#     city = models.CharField(max_length=100, blank=True)
#     country = models.CharField(max_length=100, blank=True)

# #Login 
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     # Add more fields as per your requirements

