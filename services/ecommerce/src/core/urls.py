"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.apps.account.views import UserViewSet
from src.apps.ecommerce.views import ProductViewSet, OrderViewSet, OrderItemViewSet, ShoppingCartViewSet, ShoppingCartItemViewSet
from src.core.grpc_handlers import grpc_handlers  # Register gRPC handlers

api_router = DefaultRouter()
api_router.register(r'users', UserViewSet)
api_router.register(r'products', ProductViewSet)
api_router.register(r'shopping-carts', ShoppingCartViewSet)
api_router.register(r'shopping-cart-items', ShoppingCartItemViewSet)
api_router.register(r'orders', OrderViewSet)
api_router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_router.urls)),
]

