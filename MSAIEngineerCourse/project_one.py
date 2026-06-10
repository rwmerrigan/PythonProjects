
# region Step 1: Store Customer Orders
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
print(customer_order_dictionary)
for customer_name, customer_order_tuple in customer_order_dictionary.items():
    print(f"{customer_name}: {customer_order_tuple}")
#endregion

# region Step 2: Classify Products by Category
# - Use a dictionary to map each product to its respective category
product_categories = {}

for _, product, _, category in customer_orders:
    product_categories[product] = category
# print(product_categories)

# - Create a set of unique product categories
unique_categories = set(product_categories.values())
# print("Unique Product Categories:", unique_categories)

# - Display all available product categories
categorized_products = {}

for product, category in product_categories.items():
    if category not in categorized_products:
        categorized_products[category] = []
    categorized_products[category].append(product)
print("\nProducts Classified by Category:")
for category, product in categorized_products.items():
    print(f"{category}: {product}")
#endregion

# region Step 3 Analyze Customer Orders
# - Use a loop to calculate the total amount each customer spends
customer_spending = {}
for customer, orders in customer_order_dictionary.items():
    # equivalent statement to [price for _, price, _ in orders], a "comprehension"
    # prices = []
    # for _, price, _ in orders:
    #      prices.append(price)
    total_spent = sum([price for _, price, _ in orders])
    customer_spending[customer] = total_spent
print(customer_spending)

# - If the total purchase value is above $100, classify the customer as a high-value buyer
# - If it is between $50 and $100, classify the customer as a moderate buyer
# - If it is below $50, classify them as a low-value buyer
customer_buyer_classification = {}
for customer, total_spent in customer_spending.items():
    if total_spent > 100:
        customer_buyer_classification[customer] = "High-Value Buyer"
    elif 50 <= total_spent <= 100:
        customer_buyer_classification[customer] = "Moderate Buyer"
    else:
        customer_buyer_classification[customer] = "Low-Value Buyer"

print("\nCustomer Classification Based on Spending:")
for customer, classification in customer_buyer_classification.items():
    print(f"{customer}: {classification} (Spent: ${customer_spending[customer]})")
#endregion

# region Step 4 Generate business insights
# - Calculate the total revenue per product category and store it in a dictionary
category_sales = {}
for _, product, price, category in customer_orders:
    if category not in category_sales:
        category_sales[category] = 0
    category_sales[category] += price

print("\nTotal Sales by Product Category:")
for category, total_sales in category_sales.items():
    print(f"{category}: ${total_sales}")
# - Extract unique products from all orders using a set comprehension
# this is shorthand for:
# unique_products = set()
# for _, product, _, _ in customer_orders:
#     unique_products.add(product)
unique_products = {product for _, product, _, _ in customer_orders}
print("\nUnique Products Sold:", unique_products)
# - Use a list comprehension to find all customers who purchased electronics
electronics_customers = [customer for customer, orders in customer_order_dictionary.items()
                         if any(category == "Electronics" for _, _, category in orders)]
print("\nCustomers Who Purchased Electronics:", electronics_customers)
# - Identify the top three highest-spending customers using sorting
top_spenders = sorted(customer_spending.items(), key=lambda x:x[1], reverse=True)[:3]
print("\nTop 3 Highest Spending Customers:")
for customer, total_spent in top_spenders:
    print(f"{customer}: ${total_spent}")
#endregion