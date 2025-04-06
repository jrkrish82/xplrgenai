import ssl
import requests

url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
headers = {
    "Authorization": f"Bearer AIzaSyDQaav-KRsuT8bwQy7d0scxDmY7uypVApo",
    "Content-Type": "application/json"
}
data = {
    "prompt": "Hello, world!",
    "max_tokens": 5
}

context = ssl.create_default_context()
context.options |= ssl.OP_NO_SSLv3
response = requests.post(url, headers=headers, json=data, verify=context)
print(response.json())