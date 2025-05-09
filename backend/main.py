from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm_module import analyze_performance
from backend.db import store_transaction, get_all_transactions
import os

# Define the Transaction model
class Transaction(BaseModel):
    amount: float
    category: str
    date: str
    purpose: str

app = FastAPI()

@app.post("/add_transaction/")
async def add_transaction(transaction: Transaction):
    data = transaction.dict()
    store_transaction(data)
    analysis = analyze_performance(data)
    return {"status": "stored", "analysis": analysis}

@app.get("/transactions/")
async def fetch_all():
    return get_all_transactions()

# Vercel requires an ASGI handler
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import sys

sys.stdout = sys.stderr  # Ensure Vercel outputs errors to the console

app.add_middleware(WSGIMiddleware)

# For Vercel to work, you may need to bind the FastAPI app to a wsgi callable.
if __name__ == "__main__":
    import os
    os.environ["PORT"] = str(os.environ.get("PORT", 8080))  # Ensure PORT is set for Vercel
