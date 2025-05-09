import os
import wikipedia
import pandas as pd
from processDatasets import process_datasets
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer



# Create a chatbot instance
chatbot = ChatBot(
    "QAbot", 
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=["chatterbot.logic.BestMatch"],
    database_uri="sqlite:///db.sqlite3" #stores chat history
    )

# Load the datasets, preprocess and merge them into a .csv file, IF-check to avoid redundancy
if not os.path.exists("processedDatasets.csv"):
    process_datasets()

# Load the datasets from the .csv file
dataFrame = pd.read_csv("/Users/victoria/chatbot_env/processedDatasets.csv")
datasets = dataFrame["msgContents"].tolist()

# Train the chatbot
listTrainer = ListTrainer(chatbot)
corpusTrainer = ChatterBotCorpusTrainer(chatbot)

# Train on general english conv 
corpusTrainer.train("chatterbot.corpus.english")
corpusTrainer.train("data/custom.yml")

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
