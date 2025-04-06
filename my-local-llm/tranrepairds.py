import requests

def query_deepseek(transaction):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "deepseek-r1:1.5b",
        "messages": [{"role": "user", "content": f"Repair the following transaction: {transaction}"}],
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()

def get_user_confirmation(transaction):
    # Simulate user interaction for confirmation
    print(f"Repaired transaction: {transaction}")
    confirmation = input("Is this correct? (yes/no): ")
    return confirmation.lower() == "yes"

# Example transaction
transaction = {"amount": -50, "date": "invalid-date", "description": None}

# Process the transaction
repaired_transaction = query_deepseek(transaction)
if repaired_transaction and get_user_confirmation(repaired_transaction):
    print("Transaction confirmed and repaired:", repaired_transaction)
else:
    print("Transaction repair failed or not confirmed.")