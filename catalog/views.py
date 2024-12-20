from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Item, Order, Cart, OrderItem

# Home View
def home(request):
    return render(request, 'home.html')

# Shop View
def shop(request):
    items = Item.objects.filter(status="Available")  # Fetch available items
    return render(request, 'shop.html', {'items': items})

# Add to Cart View
@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{item.name} added to cart.")
    return redirect('cart')

# Cart View
@login_required
def cart(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart_item = Cart.objects.get(id=cart_id)

        if 'update_quantity' in request.POST:
            new_quantity = request.POST.get('quantity')
            if int(new_quantity) > 0:
                cart_item.quantity = int(new_quantity)
                cart_item.save()
                messages.success(request, f"Quantity of {cart_item.item.name} updated to {new_quantity}.")
            else:
                messages.error(request, "Quantity must be a positive number.")
        elif 'remove_item' in request.POST:
            cart_item.delete()
            messages.success(request, f"{cart_item.item.name} removed from cart.")

        return redirect('cart')

    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

# Place Order View
@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)

    if cart_items.exists():
        order = Order.objects.create(user=request.user)
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity
            )
            cart_item.delete()  # Clear the cart after ordering

        messages.success(request, "Order placed successfully!")
        return redirect('profile')
    else:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

# Profile View
@login_required
def profile(request):
    ordered_items = OrderItem.objects.filter(order__user=request.user)
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'profile.html', {
        'ordered_items': ordered_items,
        'cart_items': cart_items,
    })

# User Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('shop')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

# User Registration View
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('shop')

    return render(request, 'register.html')

# Logout View
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
