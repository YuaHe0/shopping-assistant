from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    retailer = models.CharField(max_length=100)
    retailer_code = models.CharField(max_length=150)
    description = models.TextField(default="")
    category = models.CharField(max_length=100, default="")
    image_url = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

class HistoricalPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.product.name

class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="New Watchlist")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    # Add additional fields for the user profile
    bio = models.TextField(max_length=500, default='')
    location = models.TextField(max_length=500, default='')
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

