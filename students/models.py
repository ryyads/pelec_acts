from django.db import models

class Inventory(models.Model):
    item=models.CharField(max_length=100)
    number_of_item=models.IntegerField()
    

    def __str__(self):
        return self.name

# Create your models here.
