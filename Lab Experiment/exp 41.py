
# Simple Chatbot using NLP

print("Welcome to Python Chatbot")
print("Type bye to stop the chatbot")

while True:

    message = input("You: ")
    message = message.lower()

    if message == "bye":
        print("Bot: Goodbye!")
        break

    elif message == "hello":
        print("Bot: Hello! How are you?")

    elif message == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif message == "how are you":
        print("Bot: I am fine. Thank you.")

    elif message == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif message == "what is python":
        print("Bot: Python is a programming language.")

    elif message == "thank you":
        print("Bot: Welcome!")

    else:
        print("Bot: Sorry, I don't understand.")
