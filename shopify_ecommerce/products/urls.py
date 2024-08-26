from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('',views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail,name='product_detail'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart_detail, name='cart_detail'),
    path('create_order/', views.create_order, name='create_order'),
]