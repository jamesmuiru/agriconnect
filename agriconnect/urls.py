from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# ⭐️ 1. Create a simple function to handle the homepage
def home(request):
    return HttpResponse("AgriConnect Backend is Running! 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    # ⭐️ 2. Add this line to handle the root URL
    path('', home),
]
