from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Instrument(models.Model):
    symbol = models.CharField(max_length=50)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    def __str__(self):
        return self.symbol
    
