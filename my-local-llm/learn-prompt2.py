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

# Prompt - this is the only field you should change
PROMPT = """The grading function in this exercise is looking for an answer that contains the exact Arabic numerals "1", "2", and "3".
You can often get Ollama to do what you want simply by asking."""

# Get Ollama's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
    return bool(pattern.match(text))

# Print Ollama's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))