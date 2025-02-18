from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot(
    "QAbot", 
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3" #stores chat history
    )

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train on general english conv 
trainer.train("chatterbot.corpus.english")

while True: 
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Bot:",response)