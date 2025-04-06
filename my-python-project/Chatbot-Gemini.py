import openai

# Initialize the OpenAI API client
openai.api_key = 'AIzaSyDQaav-KRsuT8bwQy7d0scxDmY7uypVApo'

def chat_with_gemini(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to Chatbot powered by Gemini AI!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = chat_with_gemini(user_input)
        print(f"Gemini: {response}")

if __name__ == "__main__":
    main()

