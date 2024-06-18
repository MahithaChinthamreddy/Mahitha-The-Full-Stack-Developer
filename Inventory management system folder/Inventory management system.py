class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def update_info(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            print("Product ID already exists. Use update_stock to add more stock.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product ID not found.")

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
            if self.products[product_id].quantity < 0:
                self.products[product_id].quantity = 0
                print("Stock level cannot be negative.")
            elif self.products[product_id].quantity < 5:
                print("Low stock alert: ", self.products[product_id].name)
        else:
            print("Product ID not found.")

    def process_sale(self, product_id, quantity):
        if product_id in self.products:
            if self.products[product_id].quantity >= quantity:
                self.products[product_id].quantity -= quantity
                print("Sale processed successfully.")
                return self.products[product_id].price * quantity
            else:
                print("Not enough stock to process the sale.")
        else:
            print("Product ID not found.")

    def generate_report(self):
        print("Product Report:")
        for product_id, product in self.products.items():
            print(f"Product ID: {product_id}, Name: {product.name}, Stock: {product.quantity}, Price: {product.price}")

    def generate_low_stock_report(self, threshold=5):
        print("Low Stock Report:")
        for product_id, product in self.products.items():
            if product.quantity < threshold:
                print(f"Product ID: {product_id}, Name: {product.name}, Stock: {product.quantity}")
    
    def count_products(self):
        return len(self.products)
    
# Test cases
if __name__ == "__main__":
    # Creating initial products
    product1 = Product(1, "Laptop", "High performance laptop", 1000, 10)
    product2 = Product(2, "Smartphone", "Latest smartphone model", 800, 3)

    # Creating inventory
    inventory = Inventory()

    # Adding initial products to inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Updating product information
    product1.update_info(name="Gaming Laptop", price=1200)

    # Updating stock
    inventory.update_stock(1, -5)  # Decrease stock of Gaming Laptop
    inventory.update_stock(2, 2)   # Increase stock of Smartphone

    # Processing sale
    total_cost = inventory.process_sale(1, 3)  # Should fail due to low stock
    print("Total Cost:", total_cost)
    total_cost = inventory.process_sale(1, 2)  # Should succeed
    print("Total Cost:", total_cost)

    # Generating reports
    inventory.generate_report()
    inventory.generate_low_stock_report()

    # Removing a product
    inventory.remove_product(4)  # Remove Tablet from inventory

    # Attempt to remove a non-existent product
    inventory.remove_product(5)  # Product ID not found


    # Creating inventory
    inventory = Inventory()

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Update Product Information")
        print("3. Remove Product")
        print("4. Update Stock")
        print("5. Process Sale")
        print("6. Generate Product Report")
        print("7. Generate Low Stock Report")
        print("8. Count Products")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Product
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, description, price, quantity)
            inventory.add_product(product)

        elif choice == "2":
            # Update Product Information
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name (leave empty to keep current): ")
            description = input("Enter new product description (leave empty to keep current): ")
            price = input("Enter new product price (leave empty to keep current): ")
            if price:
                price = float(price)
            inventory.products[product_id].update_info(name, description, price)

        elif choice == "3":
            # Remove Product
            product_id = int(input("Enter product ID to remove: "))
            inventory.remove_product(product_id)

        elif choice == "4":
            # Update Stock
            product_id = int(input("Enter product ID to update stock: "))
            quantity = int(input("Enter quantity to add/subtract: "))
            inventory.update_stock(product_id, quantity)

        elif choice == "5":
            # Process Sale
            product_id = int(input("Enter product ID to sell: "))
            quantity = int(input("Enter quantity to sell: "))
            inventory.process_sale(product_id, quantity)

        elif choice == "6":
            # Generate Product Report
            inventory.generate_report()

        elif choice == "7":
            # Generate Low Stock Report
            inventory.generate_low_stock_report()
        
        elif choice == "8":
            # Count Products
            print("Total number of products:", inventory.count_products())

        elif choice == "9":
            # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
