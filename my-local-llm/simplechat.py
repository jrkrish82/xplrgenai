import requests

#system_prompt = "You are an AI assistant"
prompt = "who is einstein?"

response = requests.post('http://localhost:11434/api/generate',
json={
"model": "deepseek-r1:1.5b",
"prompt": f"{prompt}",
"stream": False
})

print(response.text)