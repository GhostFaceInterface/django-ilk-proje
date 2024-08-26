from django.shortcuts import redirect, render, get_object_or_404
from .models import Cart, CartItem, Order, Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render (request ,'products/product_list.html', {'products':products}) 

def product_detail(request, pk): # pk is the primary key of the product
    product = get_object_or_404(Product, pk=pk) #get_object_or_404 is a shortcut to get the object or return a 404 error
    return render(request, 'products/product_detail.html', {'product':product})

def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    if created:
        request.session['cart_id'] = cart.id

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart_detail')

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart,created = Cart.objects.get_or_create(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'products/cart_detail.html', {'cart_items':cart_items})


def create_order(request):
    cart = Cart.objects.get(id=request.session.get('cart_id'))
    order = Order.objects.create(
        cart=cart,
        customer_name=request.POST.get('name'),
        customer_email=request.POST.get('email')
    )
    return redirect('order_confirmation', order_id=order.id)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes = [IsAuthenticated]
