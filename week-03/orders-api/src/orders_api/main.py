from fastapi import FastAPI

app = FastAPI(title="Noor Foods Orders API")
product_list = [
    {"name": "Juice", "price": "90"},
    {"name": "chocolate", "price": "250"},
]


@app.get("/")
def read_root() -> dict[str, str]:
    return {"app": "Noor Foods Orders API", "docs": "/docs"}


@app.get("/health")
def health_status() -> dict[str, str]:
    return {"status": "OK", "docs": "/docs"}


@app.get("/products")
def list_product() -> list[dict]:
    return product_list


@app.get("health")
def check_status() -> dict[str, str]:
    return {"status": "OK", "docs": "/docs"}


# Routes and Parameters
# Examples
ORDERS = {
    "A101": {
        "id": "A101",
        "customer": "Noor Foods",
        "total": 4500,
        "status": "pending",
    },
    "A102": {
        "id": "A102",
        "customer": "Bilal Traders",
        "total": 12800,
        "status": "delivered",
    },
    "A103": {
        "id": "A103",
        "customer": "Karachi Crafts",
        "total": 2300,
        "status": "pending",
    },
}


@app.get("/orders")
def list_orders() -> list[dict]:
    return list(ORDERS.values())


# practice 01


@app.get("/orders")
def get_orders(customer: str | None = None):
    if customer:
        return [
            order
            for order in ORDERS.values()
            if order["customer"].lower() == customer.lower()
        ]

    return list(ORDERS.values())
