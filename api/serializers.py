from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    # Convert single image to list for Flutter
    imageUrls = serializers.SerializerMethodField()
    pricePerUnit = serializers.DecimalField(source='price', max_digits=10, decimal_places=2)
    farmerId = serializers.CharField(source='farmer_id')
    farmerName = serializers.CharField(source='farmer_name')

    class Meta:
        model = Product
        fields = ['id', 'farmerId', 'farmerName', 'name', 'description', 'pricePerUnit', 'quantity', 'unit', 'imageUrls', 'location', 'created_at']

    def get_imageUrls(self, obj):
        if obj.image:
            return [obj.image.url] # Return as list
        return []

class OrderSerializer(serializers.ModelSerializer):
    # Map Django snake_case to Flutter camelCase
    customerId = serializers.CharField(source='customer_id')
    customerName = serializers.CharField(source='customer_name')
    customerPhone = serializers.CharField(source='customer_phone')
    farmerId = serializers.CharField(source='farmer_id')
    farmerName = serializers.CharField(source='farmer_name')
    productId = serializers.CharField(source='product_id')
    productName = serializers.CharField(source='product_name')
    totalPrice = serializers.DecimalField(source='total_price', max_digits=10, decimal_places=2)
    deliveryLocation = serializers.JSONField(source='delivery_location')
    deliveryPersonId = serializers.CharField(source='delivery_person_id', required=False)
    deliveryPersonName = serializers.CharField(source='delivery_person_name', required=False)
    paymentRef = serializers.CharField(source='payment_ref', required=False)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
