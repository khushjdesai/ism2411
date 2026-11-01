# --- Exercise 5 Observations ---
# type("12") returns <class 'str'>
# type(12) returns <class 'int'>
#"5" + "3" produces "53" because text strings use concatenation (joining text together).
#5 + 3 produces 8 because numbers use mathematical addition.



# --- Exercise 1 ---
product = "Notebook"
unit_price = 4.99
quantity = 12
in_stock = True

print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))
# --- Exercise 2 ---
total = unit_price * quantity
print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${total:.2f}")
# --- Exercise 3 ---
user_product = input("Enter product name: ")
user_price = float(input("Enter unit price: "))
user_quantity = int(input("Enter quantity: "))
user_total = user_price * user_quantity
print(f"{user_quantity} units of {user_product} at ${user_price:.2f} each = ${user_total:.2f}")
# --- Exercise 4 ---
card_product = "Notebook"
card_price = 4.99
card_qty = 12
unit_cost = 3.29

revenue = card_price * card_qty
total_cost = unit_cost * card_qty
margin = ((revenue - total_cost) / revenue) * 100

print(f"Product: {card_product}")
print(f"Price: ${card_price:.2f}")
print(f"Qty: {card_qty}")
print(f"Revenue: ${revenue:.2f}")
print(f"Margin: {margin:.1f}%")

