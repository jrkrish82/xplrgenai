# Import python's built-in regular expression library
import re
from ollama import chat, ChatResponse, Options


# Stores the MODEL_NAME variable from the IPython store
MODEL_NAME = "deepseek-r1:1.5b"
#%store MODEL_NAME

def get_completion(prompt: str, system_prompt=""):
    response = chat(
        model=MODEL_NAME,
        options=Options(
            max_tokens=2000,
            temperature=0.0
        ),
        messages=[
            {"role": "system", "content": system_prompt},  
            {"role": "user", "content": prompt}
        ]
    )
    return response.message.content

# Prompt
#PROMPT = "Hi, how are you?"

# Print Ollama's response
#print(get_completion(PROMPT))

# Prompt
#PROMPT1 = "Can you tell me the color of the ocean?"

# Print Ollama's response
#print(get_completion(PROMPT1))

# System prompt
SYSTEM_PROMPT = "Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question."

# Prompt
PROMPT = "Why is the sky blue?"

# Print Ollama's response
print(get_completion(PROMPT, SYSTEM_PROMPT))