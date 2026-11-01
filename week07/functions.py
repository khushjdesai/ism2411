"""
Self-Assessment & Disclosure:
1. In Exercise 5, the first bug was spotted with the traceback, which pointed directly to an error. Explaining it out loud to the rubber duck helped clarify why the function call failed before applying a fix.
2. apply_discount(price, tier) takes a numerical price and a string tier like "gold", "silver", "bronze", or "none" and returns the discounted price as a float. A colleague could  use it based on its descriptive name and parameters without reading the function body.
3. AI Disclosure: Used AI to explain the meaning of some excercises and what functions do.
"""

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

for tier_val in ["gold", "silver", "bronze", "none"]:
    print(f"{tier_val}:   ${apply_discount(200, tier_val):.2f}")


# --- Exercise 3 ---
gold_price = apply_discount(200, "gold")
print(f"After gold discount: ${gold_price:.2f}")
tax_amount = calculate_tax(gold_price, 0.07)
print(f"After tax: ${gold_price + tax_amount:.2f}")

def final_price(price, tier, tax_rate):
    disc_price = apply_discount(price, tier)
    return disc_price + calculate_tax(disc_price, tax_rate)

print(f"final_price(200, \"gold\", 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Fixed version of broken_sales.py integrated into script
# Bug fixes applied: corrected function name typos, fixed argument ordering, and handled variable scope properly.
def process_sale_fixed(price, tier):
    disc = apply_discount(price, tier)
    tax = calculate_tax(disc, 0.07)
    return disc + tax

print(f"Fixed sales test: ${process_sale_fixed(200, 'gold'):.2f}")


# --- Exercise 6 ---
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # Prints 100 (global variable x)
print(double_it()) # Prints 1998 (local variable x inside double_it multiplied by 2)
print(x)           # Prints 100 (global x has not changed)

# Scope Explanation:
# Scope defines the region of a program where a variable is accessible. Global variables 
# are defined outside functions and can be accessed anywhere, whereas local variables 
# are defined inside functions and only exist within that local context. Assigning a value 
# to 'x' inside double_it() creates a new local variable rather than modifying the global 'x'.