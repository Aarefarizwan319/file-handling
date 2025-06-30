print("🤖 Hello! I am a simple Python Chatbot. (Type 'bye' to exit)\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("ChatBot: 👋 Goodbye! Have a nice day.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("ChatBot: I'm just code, but I'm working fine 😄")
    elif "your name" in user_input:
        print("ChatBot: I’m PythonBot — your assistant!")
    elif "what can you do" in user_input:
        print("ChatBot: I can answer simple questions. Try asking me something!")
    else:
        print("ChatBot: Sorry, I didn't understand that. Can you rephrase?")
