#Task 03  A product record
Prices = [850, 1200, 400]
print(Prices[2])
print(sum(Prices))

#Dictionary
productDetails = {"Name" : "Mobile Phone",
"price" : 1200,
"in_stock" : False}
print(productDetails["Name"])

# A week of sales. 
DailySales = [18500, 22300, 19800, 25400, 31200, 42800, 38600]
print("Monday Sales" , DailySales[0], "Sunday Sales", DailySales[6])
print("The sum of weekly sales", sum(DailySales))
DailyAverage = sum(DailySales)/len(DailySales)
print("The average daily sales Rs,",int(DailyAverage))
print(min(DailySales))
print(max(DailySales))

#Stock levels.
StockCount = {"pens": 120, "notebooks": 45, "staplers": 8}
StockCount["notebooks"] -=30
StockCount["markers"] = 60
print(StockCount)
print(len(StockCount))

#4. A list of orders
 
OrderList = [{"ID": "A101" , "customer": "Ali" , "total" : 500} ,
             {"ID": "A102" , "customer": "Awaiz" , "total" : 1700},
               {"ID": "A103" , "customer": "Zaib" , "total" : 900 }]
print("the second customer is", OrderList[1]["customer"])
OrderList[2]["total"] -=500
print("after 500 discoont", OrderList)
OrderList.append({"ID": "A104" , "customer": "Shakir" , "total" : 5000})
print(OrderList[0])
print(OrderList[1])
print(OrderList[2])
print(OrderList[3])

#A customer profile.
customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "order_totals": [4500, 12800, 2300],
}


print(f"City: {customer["address"]["city"]}")
print(f"Number of Orders: {len(customer["order_totals"])}")
print(f"Total Spent: Rs {sum(customer["order_totals"])}")


customer["order_totals"].append(6100)
print(f"New Total Spent after new order: Rs {sum(customer['order_totals'])}")
phone_number = customer.get("phone", "No phone number")
print(f"Phone Info: {phone_number}")




