import csv


def store_transaction(data: dict):
    # Ensure that the 'purpose' field exists
    # Default if 'purpose' is missing
    purpose = data.get('purpose', 'No purpose provided')
    with open("transactions.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data['date'], data['amount'],
                        data['category'], purpose])


def get_all_transactions():
    with open("transactions.csv", "r") as f:
        reader = csv.reader(f)
        return list(reader)
