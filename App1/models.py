from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)
    score = models.FloatField()

    def __str__(self):
        return f"Score: {self.score}"