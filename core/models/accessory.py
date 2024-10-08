from django.db import models

class Accessory(models.Model):
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc
    
    class Meta:
        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"