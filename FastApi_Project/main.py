from fastapi import FastAPI
from models import Product
app=FastAPI()

@app.get("/greet")
def greetMsg():
    return " Hello learner , Govind welcomes you !!"

products = [
    Product(id=1, name="Phone", description="smart-phone", price=15000, quantity=10),
    Product(id=2, name="Watch", description="dial-watch", price=1500, quantity=25),
    Product(id=3, name="Watch", description="smart-watch", price=3500, quantity=10),
    Product(id=4, name="Laptop", description="Coding laptop", price=65000, quantity=5)
]

@app.get("/allProduct")
def getAllProducts():
    return products

@app.get("/getPrdouct/{id}")
def getProductById(id:int):
    for i in products:
        if(i.id==id):
            return i
    return "Product not found with id ",id

@app.post("/addProduct")
def addProduct(product:Product):
    products.append(product)
    return products