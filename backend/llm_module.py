from transformers import pipeline

# Use a financial sentiment model or summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def analyze_performance(data: dict):
    # Assuming the function uses 'amount', 'category', and 'purpose' from the data
    # Add necessary analysis logic here
    return {"message": "Analysis completed", "data": data}
