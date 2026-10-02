import json
import os

def add_product(inventory):
    print("/Add New Product.")

    product_id = input("Enter Product ID: ")
    name  = input("Enter Product Name: ")

    try:
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock: "))
    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.")
        return

    for product in inventory:
        if product['product_id'] == product_id:
            print("Product ID already exists. Please use a unique Product ID.")
            return

        new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()

        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []
    
    
