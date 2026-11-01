# ==========================================
# REFLECTION QUESTIONS
# 1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
#    - It was surprising that lists use 0-based indexing (counting starting at 0 instead of 1) and that 
#      negative indices count backward from the end of the list automatically.
# 2. Describe one real business situation where a Python list would have saved you time compared to Excel.
#    - Processing hundreds of daily transaction amounts to calculate averages, find peaks, and filter sales 
#      above a threshold would take multiple manual steps or complex formulas in Excel, whereas a Python script 
#      can automate it instantly using sum(), max(), and loops.
# ==========================================

# --- EXERCISE 1: Build the list ---
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory, "|", len(inventory))


# --- EXERCISE 2: Index practice ---
print("\n--- Exercise 2 ---")
first_item = inventory[0]                  # Positive index for first
last_item = inventory[-1]                  # Negative index for last
middle_index = len(inventory) // 2         # Compute middle dynamically (5 // 2 = 2)
middle_item = inventory[middle_index]

print(f"{first_item} | {last_item} | {middle_item}")


# --- EXERCISE 3: Slicing ---
print("\n--- Exercise 3 ---")
first_three = inventory[:3]                # First three items
last_two = inventory[-2:]                  # Last two items using negative slice
every_other = inventory[::2]               # Every other item with step 2

print(f"{first_three} | {last_two} | {every_other}")


# --- EXERCISE 4: Modify ---
print("\n--- Exercise 4 ---")
inventory.append("envelope")
print("After append:", inventory)

inventory.remove("tape")
print("After remove:", inventory)

inventory.sort()
print("Final sorted list:", inventory)


# --- EXERCISE 5: Tuple comparison ---
print("\n--- Exercise 5 ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples are immutable and cannot be modified after creation.")
    print("Why tuples are useful: They protect constant data like GPS coordinates from accidental changes.")
    print("Original coords:", coords)


# --- EXERCISE 6: Average of a list of sales ---
print("\n--- Exercise 6 ---")
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")


# --- EXERCISE 7: Accumulator pattern ---
print("\n--- Exercise 7 ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)  # Reduce by 10% and round to 2 decimals
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)


# --- EXERCISE 8: Filter above threshold ---
print("\n--- Exercise 8 ---")
all_sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in all_sales:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_avg = round(sum(high_sales) / high_count, 2)

print(f"{high_sales} | Count: {high_count} | Avg: {high_avg}")