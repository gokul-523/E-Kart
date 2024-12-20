from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from catalog.models import User, Item

# Dummy user data
dummy_users = [
    {"username": "Alice123", "first_name": "Alice", "email": "alice@example.com", "password": "alice@12345"},
    {"username": "Bob456", "first_name": "Bob", "email": "bob@example.com", "password": "bob@12345"},
    {"username": "Charlie789", "first_name": "Charlie", "email": "charlie@example.com", "password": "charlie@12345"},
    {"username": "Diana01", "first_name": "Diana", "email": "diana@example.com", "password": "diana@12345"},
    {"username": "EveSecure", "first_name": "Eve", "email": "eve@example.com", "password": "eve@12345"},
    {"username": "Frank987", "first_name": "Frank", "email": "frank@example.com", "password": "frank@12345"},
    {"username": "Grace456", "first_name": "Grace", "email": "grace@example.com", "password": "grace@12345"},
    {"username": "Hank321", "first_name": "Hank", "email": "hank@example.com", "password": "hank@12345"},
    {"username": "Ivy789", "first_name": "Ivy", "email": "ivy@example.com", "password": "ivy@12345"},
    {"username": "Jake001", "first_name": "Jake", "email": "jake@example.com", "password": "jake@12345"},
]

# Populate the User table
for user_data in dummy_users:
    user_data["password"] = make_password(user_data["password"])
    user = User.objects.create(**user_data)
    print(f"Created user: {user.username}")

# Dummy item data
dummy_items = [
    {
        "name": "Wireless Earbuds",
        "description": "Noise-cancelling wireless earbuds with great sound quality.",
        "price": 59.99,
        "category": "Electronics",
        "condition": "New",
        "image": "images/wireless_earbuds.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=2),
    },
    {
        "name": "Gaming Laptop",
        "description": "High-performance laptop for gaming and productivity.",
        "price": 1200.00,
        "category": "Electronics",
        "condition": "New",
        "image": "images/gaming_laptop.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=4),
    },
    {
        "name": "Fitness Tracker",
        "description": "Track your daily activity and health metrics.",
        "price": 99.99,
        "category": "Wearables",
        "condition": "New",
        "image": "images/fitness_tracker.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=1),
    },
    {
        "name": "Smartphone",
        "description": "Latest smartphone with cutting-edge features.",
        "price": 799.99,
        "category": "Electronics",
        "condition": "New",
        "image": "images/smartphone.jpg",
        "status": "Available",
        "added_date": datetime.now(),
    },
    {
        "name": "Leather Wallet",
        "description": "Premium leather wallet with multiple compartments.",
        "price": 49.99,
        "category": "Accessories",
        "condition": "New",
        "image": "images/leather_wallet.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=3),
    },
    {
        "name": "Running Shoes",
        "description": "Comfortable and durable running shoes.",
        "price": 79.99,
        "category": "Footwear",
        "condition": "New",
        "image": "images/running_shoes.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=5),
    },
    {
        "name": "Cooking Set",
        "description": "Complete set of non-stick cookware.",
        "price": 99.99,
        "category": "Kitchenware",
        "condition": "New",
        "image": "images/cooking_set.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=6),
    },
    {
        "name": "Bluetooth Speaker",
        "description": "Portable speaker with excellent sound quality.",
        "price": 39.99,
        "category": "Electronics",
        "condition": "New",
        "image": "images/bluetooth_speaker.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=1),
    },
    {
        "name": "Graphic T-Shirt",
        "description": "Stylish t-shirt with cool graphic designs.",
        "price": 19.99,
        "category": "Clothing",
        "condition": "New",
        "image": "images/graphic_tshirt.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=2),
    },
    {
        "name": "Office Chair",
        "description": "Ergonomic office chair with lumbar support.",
        "price": 199.99,
        "category": "Furniture",
        "condition": "New",
        "image": "images/office_chair.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=4),
    },
    {
        "name": "Backpack",
        "description": "Durable backpack with multiple compartments.",
        "price": 49.99,
        "category": "Accessories",
        "condition": "New",
        "image": "images/backpack.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=3),
    },
    {
        "name": "Electric Kettle",
        "description": "Fast boiling electric kettle with auto shut-off.",
        "price": 29.99,
        "category": "Kitchen Appliances",
        "condition": "New",
        "image": "images/electric_kettle.jpg",
        "status": "Available",
        "added_date": datetime.now() - timedelta(days=5),
    },
]

# Populate the Item table
for item_data in dummy_items:
    Item.objects.create(**item_data)
    print(f"Added item: {item_data['name']}")
