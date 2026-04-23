import random
import datetime

# Response Database

responses = {
    "greetings": ["hi", "hello", "hey"],
    "how_are_you": ["how are you", "how are you doing"],
    "bye": ["bye", "goodbye", "see you"],
    "name": ["your name", "who are you"],
    "time": ["time", "current time"],
    "date": ["date", "today date"],
}

# Response Generator Function
def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in responses["greetings"]):
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help you?"])

    # How are you
    elif any(phrase in user_input for phrase in responses["how_are_you"]):
        return random.choice([
            "I'm fine, thanks!",
            "Doing great! What about you?",
            "All good here "
        ])
    # Name
    elif any(phrase in user_input for phrase in responses["name"]):
        return "I am a simple rule-based chatbot created in Python."

    # Time
    elif any(word in user_input for word in responses["time"]):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"

    # Date
    elif any(word in user_input for word in responses["date"]):
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today_date}"

    # Exit
    elif any(word in user_input for word in responses["bye"]):
        return "Goodbye! Have a nice day!"

    # Default
    else:
        return "Sorry, I didn't understand that. Can you try something else?"
# Chat Loop Function
def start_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Chatbot:", response)

        if "goodbye" in response.lower():
            break
# Run Chatbot
if __name__ == "__main__":
    start_chatbot()