from fastapi import FastAPI

app=FastAPI()
@app.get("/greet")
def greetMsg():
    return " Hello learner , Govind welcomes you !!"