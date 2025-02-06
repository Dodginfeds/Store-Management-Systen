# 🏪 Store Management System

## 📌 Overview
The **Store Management System** is a Python-based application that provides an interactive way to manage store operations. It supports sellers, customers, and admins, enabling product management, order tracking, and a loyalty program.

---

## 🚀 Features
- 🛒 **Product Management**: Sellers can add and manage products in their store.
- 👤 **Customer Shopping Experience**: Customers can browse products, add them to their cart, and earn loyalty points.
- 📦 **Order Processing**: Customers can place orders, and total sales are tracked.
- 🛠 **Admin Controls**: Admins can remove products from the store.
- 🎖 **Loyalty Program**: Customers earn and redeem points based on purchases.

---

## 🛠 Technologies Used
This project highlights fundamental **Python** concepts such as:
- **Object-Oriented Programming (OOP)**: Implements multiple classes (`Person`, `Seller`, `Customer`, `Admin`, etc.).
- **Encapsulation**: Uses methods to manage data access.
- **Inheritance & Polymorphism**: Allows different user roles (Customer, Seller, Admin) to interact differently.
- **Static & Class Methods**: Implements `calc_price()` and `get_total_orders()` for calculations.
- **Data Structures**: Uses dictionaries and lists for product and order management.

---

## 🔹 How to Use
1️⃣ **Clone the Repository**:
   ```bash
   git clone https://github.com/dodginfeds/store-management.git
   cd store-management
   ```
2️⃣ **Run the Application**:
   ```bash
   python store_manager.py
   ```

---

## 📌 Example Usage
```python
# Creating a seller and adding products
seller = Seller("Nazir Lopez", "nazirlopez123@gmail.com", "Fashion Store")
print(seller.add_product("Hoodie", 60))
print(seller.add_product("Jeans", 40))
```
🔹 **Output:**
```
Product 'Hoodie' added to Fashion Store at $60.
Product 'Jeans' added to Fashion Store at $40.
```

```python
# Creating a customer and adding items to the cart
customer = Customer("Arden Mendez", "ardenmendez123@gmail.com", points=20)
print(customer.add_to_cart("Hoodie", 60))
print(customer.add_to_cart("Jeans", 40))
```
🔹 **Output:**
```
Hoodie was added to your cart!
Jeans was added to your cart!
```

---

## 🔮 Future Enhancements
- 📊 **Database Integration**: Store product and customer data persistently.
- 💳 **Payment System**: Implement payment processing.
- 📦 **Inventory Tracking**: Automatically update stock levels.
- 📜 **Order History**: Customers can view their past purchases.

---

For any inquiries, feel free to reach out via [GitHub](https://github.com/dodginfeds).
