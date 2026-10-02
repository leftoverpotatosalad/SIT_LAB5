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
    try:
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with empty inventory.")

        return []


def save_inventory(inventory):
    file = open("inventory.json", "w")

    json.dump(inventory, file, indent=4)

    file.close()

    print("Inventory saved successfully to inventory.json.")

def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("No products in inventory.")

    else:
        for product in inventory:
            print(
                "ID:", product["id"],
                "| Name:", product["name"],
                "| Price: $" + format(product["price"], ".2f"),
                "| Stock:", product["stock"]
            )

    print("------------------------------------------------")

    def update_stock(inventory):
        print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:

        if product["id"] == product_id:

            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            try:
                new_stock = int(input("New Stock Quantity: "))

            except ValueError:
                print("Invalid stock quantity.")
                return

            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")

