import json


def add_product(inventory):
    print("\nAdd New Product.")

    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")

    try:
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock: "))

    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.")
        return


    for product in inventory:
        if product["id"] == product_id:
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


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:

        if product["id"] == product_id:

            print("Product Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price: $" + format(product["price"], ".2f"))
            print("Stock:", product["stock"])
            print("------------------------------------------------")

            return

    print("Product not found.")


def main():

    inventory = load_inventory()

    while True:

        print("\n========================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("========================================")

        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            display_all(inventory)

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")

            save_inventory(inventory)

            print("Thank you for using Inventory Management System.")
            print("Program terminated.")

            break

        else:
            print("Invalid option. Please enter 1-6.")


main()