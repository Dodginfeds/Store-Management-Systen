# ---------------------------------------------
# Store Management System
# ---------------------------------------------
# This system manages:
# 1. Sellers who can add and manage products.
# 2. Customers who can add products to their cart and redeem loyalty points.
# 3. Orders to track total sales.
# 4. Admins who can remove products from the store.
# ---------------------------------------------

# ---------------------------------------------
# Base Person Class
# ---------------------------------------------

class Person:
    """
    Represents a person with a name and email.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        """
        Displays basic information about the person.
        """
        return f"Name: {self.name} | Email: {self.email}"

# ---------------------------------------------
# Order Helper Class
# ---------------------------------------------

class OrderHelp:
    """
    A helper class for order-related calculations.
    """

    @staticmethod
    def calc_price(cart):
        """
        Calculates the total price of items in a cart.
        """
        return sum(price for _, price in cart)

# ---------------------------------------------
# Loyalty Program Class
# ---------------------------------------------

class LoyaltyProgram:
    """
    Represents a simple loyalty points system for customers.
    """

    def __init__(self, points=0):
        self.points = points

    def redeem_points(self):
        """
        Displays the total loyalty points a customer has.
        """
        return f"You have {self.points} loyalty points!"

# ---------------------------------------------
# Seller Class
# ---------------------------------------------

class Seller(Person):
    """
    Represents a seller who can add and manage products.
    """

    def __init__(self, name, email, store_name):
        super().__init__(name, email)
        self.store_name = store_name
        self.products = {}

    def add_product(self, product_name, price):
        """
        Adds a product to the seller's store.
        """
        self.products[product_name] = price
        return f"Product '{product_name}' added to {self.store_name} at ${price}."

    def display_products(self):
        """
        Displays all available products in the store.
        """
        if not self.products:
            return "No products available in the store."
        return "\n".join([f"Product: {product} | Price: ${price}" for product, price in self.products.items()])

    def get_role(self):
        """
        Returns the role of the seller.
        """
        return f"{self.name} is a Seller."

# ---------------------------------------------
# Customer Class
# ---------------------------------------------

class Customer(Person, LoyaltyProgram):
    """
    Represents a customer who can shop and earn loyalty points.
    """

    def __init__(self, name, email, points=0):
        Person.__init__(self, name, email)
        LoyaltyProgram.__init__(self, points)
        self.cart = []

    def get_role(self):
        """
        Returns the role of the customer.
        """
        return f"{self.name} is a Customer."

    def display_cart(self):
        """
        Displays the items currently in the customer's cart.
        """
        if not self.cart:
            return "Your cart is empty."
        return "\n".join([f"Product: {product} | Price: ${price}" for product, price in self.cart])

    def add_to_cart(self, product_name, price):
        """
        Adds an item to the customer's cart.
        """
        self.cart.append((product_name, price))
        return f"{product_name} was added to your cart!"

# ---------------------------------------------
# Order Class
# ---------------------------------------------

class Order:
    """
    Represents an order placed by a customer.
    """

    total_orders = 0  # Tracks total number of orders

    def __init__(self, customer, store_name):
        self.customer = customer
        self.store_name = store_name
        self.orders = customer.cart
        self.total = OrderHelp.calc_price(self.orders)
        Order.total_orders += 1

    @classmethod
    def get_total_orders(cls):
        """
        Retrieves the total number of orders placed.
        """
        return f"Total orders placed: {cls.total_orders}"

    def calculate_total(self):
        """
        Calculates the total cost of the customer's order.
        """
        return f"Order total is ${self.total}."

# ---------------------------------------------
# Admin Class
# ---------------------------------------------

class Admin(Seller):
    """
    Represents an admin who can manage store products.
    """

    def __init__(self, name, email, store_name):
        super().__init__(name, email, store_name)

    def remove_product(self, product_name):
        """
        Removes a product from the store.
        """
        if product_name in self.products:
            del self.products[product_name]
            return f"Product '{product_name}' removed from {self.store_name}."
        return f"Product '{product_name}' not found in {self.store_name}."

# ---------------------------------------------
# Example Usage
# ---------------------------------------------

# Creating a seller and adding products
seller = Seller("Nazir Lopez", "nazirlopez123@gmail.com", "Fashion Store")
print(seller.add_product("Hoodie", 60))
print(seller.add_product("Jeans", 40))
print("\n--- Seller's Products ---")
print(seller.display_products())

# Creating a customer and adding items to the cart
customer = Customer("Arden Mendez", "ardenmendez123@gmail.com", points=20)
print("\n--- Customer Info ---")
print(customer.display_info())
print(customer.add_to_cart("Hoodie", 60))
print(customer.add_to_cart("Jeans", 40))
print("\n--- Customer's Cart ---")
print(customer.display_cart())
print(customer.redeem_points())

# Placing an order
order = Order(customer, "Fashion Store")
print("\n--- Order Details ---")
print(order.calculate_total())
print(Order.get_total_orders())

# Admin actions
admin = Admin("Admin User", "admin@example.com", "Tech Store")
print("\n--- Admin Actions ---")
print(admin.remove_product("Hoodie"))
print("\n--- Updated Products ---")
print(seller.display_products())
