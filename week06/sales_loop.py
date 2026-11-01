# self-assessment questions answer
# 1. The accumulator pattern is a programming technique used to build up a resultlike a sum, count, or maximum by looping through 
# a collection step-by-step. The three key steps include initialization which is setting a starting value before the loop starts. Then, updating which is modifying
# the accumulator inside the loop. This matters because it incorporates each individual item into the running total. Lastly. finalizing which is using 
# or displaying the final result after the loop finishes. 

# 2. The while loop version required more lines of code and manual variable managementcompared to the for loop, which handles iteration 
# automatically. For trade offs, a for loop is cleaner and safer. A while loop is useful when you aren't iterating over a fixed collection 
# or need custom index control, but it is more prone to bugs.
#
# 3. In a summer job analyzing customer checkout data, I would use a loop to compute the average order value for an e-commerce store. 
# The list would contain daily transaction amounts, I would accumulate both a running total and a transaction count, and at the end, 
# I would print the total revenue and the overall average order value.


# Base sales data for all exercises
sales = [120, 80, 250, 175, 90, 410, 60, 215]

# ---Exercise 1 ---
total = 0       # initialize
for sale in sales:
    total += sale   # update
print(f"Total: ${total}")

print() # Blank line for readability

# ---Exercise 2 ---
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1
average = total / count

print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

print()

# ---Exercise 3---
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

print()

# ---Exercise 4---
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

print()

# ---Exercise 5--- 
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

print()

#  ---Exercise 6---
total = 0
i = 0            # index
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total: ${total}")
# Note: In production, the for loop version is preferred because it is cleaner, 
# less prone to infinite loops or off-by-one errors, and more Pythonic.

print()

#---Exercise 7---
for sale in sales:
    if sale >= 200:
        discount = 0.10
        discount_text = "10%"
    elif sale >= 100:
        discount = 0.05
        discount_text = "5%"
    else:
        discount = 0.00
        discount_text = "0%"
    
    discounted_price = sale * (1 - discount)
    print(f"${sale} → {discount_text} discount → ${discounted_price:.2f}")