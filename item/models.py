from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Catagories'
        ordering = ('name' ,)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    catagory = models.ForeignKey(Catagory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    quantity = models.IntegerField(default=1)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name