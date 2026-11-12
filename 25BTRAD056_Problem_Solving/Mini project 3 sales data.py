products = {}
def add_product():
    name = input("Enter product name: ")

    if name not in products:
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter price per unit: "))
        products[name] = {"quantity": quantity, "price": price}
        print("Product added successfully!")
    else:
        print("Product already exists.")

def update_sales():
    name = input("Enter product name: ")

    if name in products:
        quantity = int(input("Enter additional quantity sold: "))
        products[name]["quantity"] += quantity
        print("Sales updated successfully!")
    else:
        print("Product not found.")

def display_sales():
    print("\n--- Sales Records ---")

    for name, details in products.items():
        revenue = details["quantity"] * details["price"]
        print("Product:", name)
        print("Quantity Sold:", details["quantity"])
        print("Price:", details["price"])
        print("Revenue:", revenue)

def total_sales():
    total = 0

    for details in products.values():
        total += details["quantity"] * details["price"]

    print("Total Sales Revenue: Rs.", total)

def highest_selling():
    if products:
        highest = max(products, key=lambda x: products[x]["quantity"])
        print("Highest Selling Product:", highest)
        print("Quantity Sold:", products[highest]["quantity"])
    else:
        print("No sales records available.")

def menu():
    while True:
        print("\n===== SALES DATA ANALYZER =====")
        print("1. Add Product")
        print("2. Update Sales")
        print("3. Display Sales")
        print("4. Calculate Total Sales")
        print("5. Highest Selling Product")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            update_sales()
        elif choice == "3":
            display_sales()
        elif choice == "4":
            total_sales()
        elif choice == "5":
            highest_selling()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")
menu()
