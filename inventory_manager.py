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

    
    
