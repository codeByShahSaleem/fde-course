orders = [
       {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"}
]

delivered_revenue = 0

for order in orders:
    if order["status"] == "delivered":
        delivered_revenue = delivered_revenue+order["total"]

print(f"Delivered revenue: Rs {delivered_revenue}")