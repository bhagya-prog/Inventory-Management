import csv
import os
import matplotlib.pyplot as plt

def load_inventory():
    inventory = []
    if os.path.exists("inventory.csv"):
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    try:
                        item = {
                            "name": row[0],
                            "price": float(row[1]),
                            "quantity": int(row[2])
                        }
                        inventory.append(item)
                    except ValueError as e:
                        print(f"Error converting data: {e}")
                else:
                    print("Invalid row format: Each row should have 3 elements.")
    return inventory

def save_inventory(inventory):
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for item in inventory:
            writer.writerow([item["name"], item["price"], item["quantity"]])

def view_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for item in inventory:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

def plot_inventory(inventory):
    if not inventory:
        print("No inventory data to plot.")
        return

    # Bar chart 
    names = [item["name"] for item in inventory]
    quantities = [item["quantity"] for item in inventory]

    plt.figure(figsize=(8, 6))
    plt.bar(names, quantities, color='blue')
    plt.title("Inventory Quantity")
    plt.xlabel("Item")
    plt.ylabel("Quantity")
    plt.show()

    # Line chart 
    plt.figure(figsize=(8, 6))
    plt.plot(quantities, marker='o', linestyle='-', color='purple')
    plt.title("Quantity Over Items")
    plt.xlabel("Item Index")
    plt.ylabel("Quantity")
    plt.show()

    # Histogram 
    prices = [item["price"] for item in inventory]
    plt.figure(figsize=(8, 6))
    plt.hist(prices, bins=10, color='green', edgecolor='black')
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()

def boss_interface(inventory):
    while True:
        print("\nBoss Interface")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Plot Inventory Charts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            delete_item(inventory)
        elif choice == "4":
            view_inventory(inventory)
        elif choice == "5":
            plot_inventory(inventory)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def add_item(inventory):
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item = {"name": name, "price": price, "quantity": quantity}
    inventory.append(item)
    save_inventory(inventory)
    print(f"{name} added to the inventory.")

def update_item(inventory):
    name = input("Enter the name of the item to update: ")
    for item in inventory:
        if item["name"] == name:
            item["price"] = float(input("Enter the new price: "))
            item["quantity"] = int(input("Enter the new quantity: "))
            save_inventory(inventory)
            print(f"{name} updated in the inventory.")
            return
    print(f"{name} not found in the inventory.")

def delete_item(inventory):
    name = input("Enter the name of the item to delete: ")
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            save_inventory(inventory)
            print(f"{name} deleted from the inventory.")
            return
    print(f"{name} not found in the inventory.")

def employee_interface(inventory):
    while True:
        print("\nEmployee Interface")
        print("1. View Inventory")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

#Main 
inventory = load_inventory()

while True:
    print("\nInventory Management System")
    print("1. Boss Interface")
    print("2. Employee Interface")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        boss_interface(inventory)
    elif choice == "2":
        employee_interface(inventory)
    elif choice == "3":
        print("Thank you for using the Inventory Management System.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
