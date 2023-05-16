from django.urls import path, include

urlpatterns = [
    path('api/', include('Products.urls')),
    path('api/', include('Users.urls')),
]