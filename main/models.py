import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('JERSEY', 'Jersey'),
        ('SEPATU', 'Sepatu Basket'),
        ('BOLA', 'Bola Basket'),
        ('APPAREL', 'Pakaian & Apparel'),
        ('AKSESORIS', 'Aksesoris'),
        ('KOLEKTIBEL', 'Kolektibel & Merchandise'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # title = models.CharField(max_length=255)
    # content = models.TextField()
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    # thumbnail = models.URLField(blank=True, null=True)
    product_views = models.PositiveIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # is_featured = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    rating_count = models.IntegerField(default=0)
    total_rating_sum = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    @property
    # def is_news_hot(self):
    #     return self.product_views > 20
        
    # def increment_views(self):
    #     self.stock+= 1
    #     self.save()
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()
    
    def is_in_stock(self):
        return self.stock > 0
        
    def decrease_stock(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            return True
        return False

    def increase_stock(self, quantity=1):
        if quantity > 0:
            self.stock += quantity
            self.save()

    def set_stock(self, new_stock_level):
        if new_stock_level >= 0:
            self.stock = new_stock_level
            self.save()

    def update_rating(self, new_rating: int):
        if 1 <= new_rating <= 5:
            self.total_rating_sum += new_rating
            self.rating_count += 1
            self.rating = round(self.total_rating_sum / self.rating_count, 2)
            self.save()