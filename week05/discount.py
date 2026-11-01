#self assessment questions 
#1 - For order_total = 350: It first checks if total >= 500 (False).
#1 Then it moves to the next condition and checks if total >= 200(True), which applies a 10% tier discount. 
#1 The remaining elif and else blocks are skipped.

#2 The condition `if total > 100 and total < 500:` requires both conditions to be true simultaneously.
#2 Two separate `if` statements would execute independently and if they overlap or modify variables without an `elif` structure, 
#2 it could lead to logical errors or duplicate overrides.

#3 Day-to-day tiered systems include shipping fee calculations, credit card rewards programs, and income tax brackets. 
# Knowing Python conditionals helps us understand how boundary conditions (like `>=` vs `>`) govern sequential business rules and decision trees.



#excercise 1 
#starter code from lab5 
total = float(input("Enter cart total: $"))

# Add your if/elif/else here
if total >= 500: 
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0

#discount = 0  # replace with correct logic
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")



#excercise 2 
if final > 1000: # strictly greater than. 
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")



#excercise 3

region = "South"
total = 250

if total >= 500: 
    tier_discount = 0.15
elif total >= 200:
    tier_discount = 0.1
elif total >= 100:
    tier_discount = 0.05
else:
    tier_discount = 0

if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")
else:
    extra_discount = 0

total_discount = tier_discount + extra_discount
final = total * (1 - total_discount)
print(f"Final discount: {total_discount*100:.0f}%")
print(f"Final price: ${final:.2f}")


#excercise 4
customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

#the flat version is easier to read as flat is readable and testable. It can verify all 
# conditions independently without nesting the test cases three levels deep.

#excercise 5

amount = 0

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE — REVIEW REQUIRED")


#excercise 6

total_spent_this_year = 2500
orders_this_year = 6 
has_outstanding_balance = False # bool

vip_upgrade = (total_spent_this_year > 2000 or orders_this_year > 10) and not has_outstanding_balance
print(f"VIP Upgrade Status: {vip_upgrade}")