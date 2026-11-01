# Revenue, Margins, and a Discount Calculator

#Excercise 1:
price = 50
quantity = 12
revenue = price * quantity
# ,.2f has two jobs -> thousands seperator and EXACTLY 2 decimal places

print(f"Revenue: ${revenue:,.2f}")

#Excercise 2:
cost = 32
price = 50
margin = (price - cost) / price # margin stays as a decimal
print(f"Margin: {margin:.1%}")

# excercise 3: Boolean logic
#Product A wins if margin_a> margin_b
#Product A margin 60%, Product B margin (80-60)/80 = 25%
margin_a = 0.60
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

#Excercise 4: Logic combo

is_premium = price > 100 and margin > 0.3 # Remember to review basic logic operators: and, or, not 

price = 150
margin = .2
is_premium = price > 100 and margin > 0.3 # Remember to review basic logic operators: and, or, not
print(f"Is premium (Second check): {is_premium}") 

#Excercise 5: Division + Mod

print(17/5) #3.4
print(17//5) #3
print(17%5) #2


#Excercise 6

def calc_discount(price, rate): 
    return price * (1-rate) # gives us the answer 

print(calc_discount(100, int(8/100))) #80.0 

discounted_pct = 20 
discounted_rev = revenue * (1 - discounted_pct / 100)

print(discounted_rev)

# inputs, name, retail_price, cost, quantity_sold, discount_pct (whole number between 0 and 100)

product = input("Enter the product name: ")
retail_price = float(input("Enter the retail price: "))
quantity_sold = int(input("Enter the quantity sold: "))
discounted_pct = int(input("Enter the discount percentage: "))
cost = float(input("Enter the cost: "))
print('='*50)

revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1-discounted_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

# output
print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")






#Excercise 7:

BOX_SIZE = 24 # ALL UPPER CASE MEANS CONSTANTS 
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE #floor div. is not abstract math
loose_items = items_ordered % BOX_SIZE #modulo is not abstract math
exact_fit = loose_items == 0
print(f"Full boxes: {full_boxes}")
print(f"Loose Items: {loose_items}")
print(f"Exact fit: {exact_fit}")

#Stretch A
retail_price = 50
cost = 32
fixed_costs = 1000
contribution = retail_price - cost
whole_units = int(fixed_costs // contribution)

print(f"Whole units: {whole_units}")