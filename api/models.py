from django.db import models

class Product(models.Model):
    farmer_id = models.CharField(max_length=100)
    farmer_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    
    # Store single image for now (Simpler for migration)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # ⭐️ Stores {'lat': -1.2, 'lng': 36.8}
    location = models.JSONField(default=dict) 
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('inTransit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    
    farmer_id = models.CharField(max_length=100)
    farmer_name = models.CharField(max_length=100)
    
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    
    quantity = models.FloatField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # ⭐️ Stores Delivery Location Map
    delivery_location = models.JSONField(default=dict)
    
    delivery_person_id = models.CharField(max_length=100, blank=True, null=True)
    delivery_person_name = models.CharField(max_length=100, blank=True, null=True)
    
    payment_ref = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
