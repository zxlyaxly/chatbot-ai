# Simple rule-based chatbot in Python
def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm here to help you!",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure! I can assist you with general queries. What do you need help with?",
        "what is your name": "I am a Python Chatbot!",
      
    }

    # Convert user input to lowercase for consistency
    user_input = user_input.lower()

    # Check if the user input matches a predefined response
    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I don't understand that. Can you please rephrase?"

# Chat loop
if __name__ == "__main__":
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_message)
        print(f"Chatbot: {response}")

