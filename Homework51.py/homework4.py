class Warehouse:
    def __init__(self):
        self.current_products = {
            "Milk": {"qty": 20, "category": "Dairy", "expiry": "2025-01-10"},
            "Shampoo": {"qty": 15, "category": "Personal Care", "expiry": "2027-03-12"},
            "Rice": {"qty": 50, "category": "Grains", "expiry": "2030-08-01"}
        }
    def add_product(self):
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        category = input("Enter category: ")
        expiry = input("Enter expiry date (YYYY-MM-DD): ")
        self.current_products[name] = {
            "qty": qty,
            "category": category,
            "expiry": expiry
        }
        print(f"{name} added with {qty} units in category '{category}'.")
    def expiry_products(self):
        today = input("Enter today's date (YYYY-MM-DD): ")
        expired_list = []
        for name, details in self.current_products.items():
            if details["expiry"] < today:
                expired_list.append(name)
        for item in expired_list:
            self.current_products.pop(item)
        print(f"Expired products removed are {expired_list}")
    def identify_low_products(self):
        print("Checking for low-stock products...")
        for name, values in self.current_products.items():
            if values["qty"] <= 30:
                print(f"Low stock detected for {name}. Restocking 100 units.")
                values["qty"] += 100
            else:
                print(f"{name} has sufficient stock ({values['qty']} units).")
bar = Warehouse()
while True:
    print("\n--- Warehouse Management System ---")
    print("1. Add products to the warehouse")
    print("2. Remove expired products")
    print("3. Identify shortages")
    print("4. Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        bar.add_product()
    elif choice == 2:
        bar.expiry_products()
    elif choice == 3:
        bar.identify_low_products()
    elif choice == 4:
        print("Thanks for using our service.")
        break
    else:
        print("Invalid input.")









