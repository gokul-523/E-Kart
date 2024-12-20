from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),  # Added trailing slash for consistency
    path('register/', views.register, name='register'),  # Added trailing slash
    path('login/', views.user_login, name='login'),  # Added trailing slash
    path('logout/', views.logout_user, name='logout'),  # Added trailing slash
    path('profile/', views.profile, name='profile'),  # Added trailing slash
    path('cart/', views.cart, name='cart'),  # Added trailing slash
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Fixed duplicate
    path('checkout/', views.place_order, name='place_order'),  # Corrected and added place_order path
]
