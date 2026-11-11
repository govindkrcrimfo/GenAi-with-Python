import os 
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

#create the agents is going to manage the tool calling loop
from langchain.agents import create_agent

load_dotenv()

# our data > imagine it is our order database
ORDERS = {
"ORD-1001": {"item": "Wireless mouse", "status": "shipped", "amount": 1499},
"ORD-1002": {"item": "Mechanical keyboard", "status": "packed", "amount": 4999},
"ORD-1003": { "item": "Laptop", "status" : "out for delivery" , "amount":50000},
"ORD-1004": {"item" : "Iphone", "status":"order in progress", "amount":75000}
}

# imagine we have warehouse stock
STOCK = {"wireless mouse": 12, 
         "mechanical keyboard": 0, 
         "usb hub": 34 ,
         "lapton":5,
         "Iphone":15
         }

@tool
def order_status(order_id:str)->str:
    """Get the status and amount of an order using its id, for example ORD-1001."""
    order=ORDERS.get(order_id.upper())
    if order is None:
        return f"No order found with id {order_id}."
    
    return f"{order['item']}, status {order['status']}, amount {order['amount']} rupees"

@tool
def check_stock(item:str)->str:
    """Check how many units of an item are left in the warehouse."""
    count=STOCK.get(item.lower())
    if count is None:
        return f"{item} is not in the catalogue."
    return f"{count} units of {item} in stock"

@tool
def apply_discount(amount: float, percent: float) -> float:
    """Apply a discount percentage to an amount and return the new amount."""
    return round(amount - (amount * percent / 100), 2)

@tool
def delivery_days(pin_code: str) -> str:
    """Estimate delivery time for an Indian pin code."""
    metro = {"400001", "110001", "560001"}
    return "2 days" if pin_code in metro else "5 days"

agent=create_agent(
     model=ChatGroq(
        model="qwen/qwen3.8-27b"
    ),
    tools=[order_status,check_stock,apply_discount,delivery_days],
    system_prompt=(
        "You are a support assistant for an online store. "
        "Use the tools for anything about orders, stock, pricing or delivery. "
        "Never guess a number, look it up."
    ),
)

def ask(question):
    print("Q:", question)
    result = agent.invoke({"messages": [
        {"role": "user",
          "content": question}
        ]})
    print("A:", result["messages"][-1].content)
    print("-" * 90)

ask("What is status of order ORD-1003")
ask("Do you have mmechanical keyboard in stock ? ")
ask("when the mechanical keyboard available again ? ")



