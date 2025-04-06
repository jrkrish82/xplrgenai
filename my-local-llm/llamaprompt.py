import ollama

# Initialize the local LLaMA model
model_path1 = r"C:\Users\113720\.ollama\models\manifests\registry.ollama.ai\library\llama2"
model = ollama.LocalModel(model_path=model_path1)

# Define the system prompt
system_prompt = "You are a helpful assistant."

# Define the user prompt
user_prompt = "What is the capital of France?"

# Combine the prompts
combined_prompt = f"{system_prompt}\n\n{user_prompt}"

# Generate a response from the model
response = model.generate(prompt=combined_prompt)

# Print the response
print(response)