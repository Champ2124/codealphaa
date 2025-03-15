#pip install nltk
import nltk
import random
from nltk.chat.util import Chat, reflections

#  Some basic patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"how are you?", ["I'm doing great, thanks for asking!", "I'm good, how about you?"]),
    (r"what is your name?", ["I am a chatbot created by you!", "You can call me Chatbot!"]),
    (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]),
    (r"bye|exit|quit", ["Goodbye!", "See you later!", "Take care!"]),
    (r"(.*)", ["Sorry, I didn't understand that.", "Can you please rephrase?"])
]

# A chatbot class
class BasicChatbot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)

    def start_conversation(self):
        print("Hi, I'm your chatbot. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Goodbye!")
                break
            response = self.chatbot.respond(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    nltk.download('punkt')  
    chatbot = BasicChatbot()
    chatbot.start_conversation()