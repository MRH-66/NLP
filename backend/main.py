from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.llm_module import analyze_performance
from backend.db import store_transaction, get_all_transactions
from pydantic import BaseModel

# Define the Transaction model


class Transaction(BaseModel):
    amount: float
    category: str
    date: str
    purpose: str


app = FastAPI()

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/add_transaction/")
async def add_transaction(transaction: Transaction):
    data = transaction.dict()
    store_transaction(data)
    analysis = analyze_performance(data)
    return {"status": "stored", "analysis": analysis}


@app.get("/transactions/")
async def fetch_all():
    return get_all_transactions()
