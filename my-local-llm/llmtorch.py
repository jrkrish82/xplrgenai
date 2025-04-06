from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the local LLaMA model and tokenizer
model_path1 = r"C:\Users\113720\.ollama\models\blobs"
model = AutoModelForCausalLM.from_pretrained(model_path1)
tokenizer = AutoTokenizer.from_pretrained(model_path1)

# Define the system prompt
system_prompt = "You are a helpful assistant."

# Define the user prompt
user_prompt = "What is the capital of France?"

# Combine the prompts
combined_prompt = f"{system_prompt}\n\n{user_prompt}"

# Tokenize the input
inputs = tokenizer(combined_prompt, return_tensors="pt")

# Generate a response from the model
with torch.no_grad():
    outputs = model.generate(**inputs, max_length=100)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)