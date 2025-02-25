import wikipedia
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



# Create a chatbot instance
chatbot = ChatBot(
    "QAbot", 
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=["chatterbot.logic.BestMatch"],
    database_uri="sqlite:///db.sqlite3" #stores chat history
    )

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot) 

# Train on general english conv 
trainer.train("chatterbot.corpus.english")
trainer.train("data/custom.yml")

def chatbot_response(user_input):
    try:
        return wikipedia.summary(user_input, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many options: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find an answer."


print("Chatbot is ready! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user_input))