from django.db import models

class Pizza(models.Model):

    name = models.CharField(max_length=20)
    base_price = models.FloatField(default=5.00)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        self.name = name

    def total_price(self):
        pass

class Topping(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    pizza = models.ForeignKey(Pizza)

    def __str__(self):
        self.name = name