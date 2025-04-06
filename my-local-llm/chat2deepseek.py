import requests

url = "http://localhost:11434/api/generate"
payload = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Hi, how are you?",
}

response = requests.post(url, json=payload)
if response.status_code == 200:
    result = response.json()
    print("Model Response:", result)
else:
    print("Failed to get a response from the model:", response.status_code)