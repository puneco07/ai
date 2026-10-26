def chatbot(user_input):
    user_input=user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I AM GOOD, THANK YOU! How can I assist you today?"
    elif "your name" in user_input:
        return "I am a simple chatbot."
    elif "thank" in user_input or "thank you" in user_input:
        return "You're welcome!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"    
                                                                    




print("Simple Chatbot")
print("Type 'bye' or 'exit' to stop")

while True:
    user_input=input("You:")
    response=chatbot(user_input)
    print("Bot:",response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break