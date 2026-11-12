#Task 04 Free delivery
total = 6200
city = "lahore"
if total >= 5000 and city == "lahore":
    print("Your Delivery is Free")
else:
    print("Delivery Charges: 350")

# 2. Grades. 
GivenMarks =  49
if GivenMarks >= 80:
    print("Grade A")
elif GivenMarks >=65 or GivenMarks <=79:
    print("Grade B")
elif GivenMarks >=50 or GivenMarks <=64:
    print("Grade C")
else:
    print("failed")

# 3. Stock check.

stock =  12
quantity = 10
if quantity <= 0:
    print("Invalid quantity")
elif quantity > stock:
    print("Only 12 left in stock")
else:
    remains=stock-quantity
    print("comfirmed!" ,remains ,"left after this order")

# 4. Shipping rules

weight_kg = 100
order_total= 209
city= "islamabad"

if order_total > 10000:
    print("Shipment Free!")
elif order_total < 10000 and city in ["islamabad","karachi","lahore"] and weight_kg <= 5:
    print("the shipment charges are 200")
elif order_total < 10000 and city in ["islamabad","karachi","lahore"] and weight_kg > 5:
    print("the shipment charges are 400")
elif order_total < 10000 and weight_kg <= 5:  
    print("the shipment charges are 350")
else:  
    print("the shipment charges are 700")

 # 5. Ticket triage.

plan = "normal"
HoursOpen =6
message = "I want a Refund"

if plan == "normal" and HoursOpen > 4:
    print("urgent")
elif "refund" in message.lower() or "charged twice" in message.lower() or (plan == "pro" and HoursOpen > 24):
    print("High")
else:
    print("Normal")
