from django.db import models
from tabnanny import verbose
# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.pizza_name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField() 

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.text