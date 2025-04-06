# chatbot.py

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I don't understand that."
    }
    
    # Convert user input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()
    
    # Return the response if it exists, otherwise return the default response
    return responses.get(user_input, responses["default"])

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

    