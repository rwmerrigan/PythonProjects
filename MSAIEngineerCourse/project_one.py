
# Step 1 Store customer orders
# - Create a list of customer names
customer_names = ["Cassandra", "Liliana", "Jerod", "Rick", "Siobhan", "Thomas"]

# - Store each customer's order details (customer name, product, price, category) as tuples inside a list
customer_orders = [
    ("Liliana", "Jeans", 50, "Clothing"),
    ("Rick", "Osmose", 1600, "Synthesizer"),
    ("Thomas", "Hat", 20, "Clothing"),
    ("Liliana", "Glasses", 20, "Clothing"),
    ("Jerod", "Apples", 10, "Grocery"),
    ("Siobhan", "Laptop", 1500, "Electronics"),
    ("Cassandra", "Candle", 10, "Home Essentials"),
    ("Rick", "Gum", 5, "Grocery"),
    ("Jerod", "Stapler", 15, "Office Supplies"),
    ("Siobhan", "The Shining", 25, "Books")
]

# - Use a dictionary where keys are customer names and values are lists of ordered products
customer_order_dictionary = {}

for order in customer_orders:
    # This is a python way to equate variables in a list I believe, basically 
    # assigning the values in the tuple to the comma separated values in order
    # shown here
    customer, product, price, category = order
    if customer not in customer_order_dictionary:
        # create an empty list with customer name as key ready to be 
        # populated with customer order data in a list of tuples
        customer_order_dictionary[customer] = []
    customer_order_dictionary[customer].append((product, price, category))
    
for customer_name, customer_order_tuple in customer_order_dictionary.items():
    print(f"{customer_name}: {customer_order_tuple}")

# Step 2 Classify products by category
# - Use a dictionary to map each product to its respective category
product_categories = {}

for _, product, _, category in customer_orders:
    product_categories[product] = category
# print(product_categories)
# {'Jeans': 'Clothing', 'Osmose': 'Synthesizer', 'Hat': 'Clothing', 'Glasses': 'Clothing', 
# 'Apples': 'Grocery', 'Laptop': 'Electronics', 'Candle': 'Home Essentials', 'Gum': 'Grocery', 
# 'Stapler': 'Office Supplies', 'The Shining': 'Books'}

# - Create a set of unique product categories
unique_categories = set(product_categories.values())
# print("Unique Product Categories:", unique_categories)
# Unique Product Categories: {'Office Supplies', 'Clothing', 'Home Essentials', 'Synthesizer', 
# 'Grocery', 'Books', 'Electronics'}

# - Display all available product categories
categorized_products = {}

for product, category in product_categories.items():
    if category not in categorized_products:
        categorized_products[category] = []
    categorized_products[category].append(product)
print("\nProducts Classified by Category:")
for category, product in categorized_products.items():
    print(f"{category}: {product}")

# Step 3 Analyze customer orders
# - Use a loop to calculate the total amount each customer spends
# - If the total purchase value is above $100, classify the customer as a high-value buyer
# - If it is between $50 and $100, classify the customer as a moderate buyer
# - If it is below $50, classify them as a low-value buyer

