# ===================================================================================
# NOTE: This file will load two datasets, preprocess and merge them into a .csv file
# If you want to add more datasets using the load_dataset() function, edit here
# ===================================================================================
from datasets import load_dataset
import pandas as pd

def process_datasets():    
    # Load the training splits
    everyday_conversations = load_dataset("HuggingFaceTB/everyday-conversations-llama3.1-2k", split="train")
    topical_chat = load_dataset("Conversational-Reasoning/Topical-Chat", split="train")

    # Insert into Pandas' DataFrame
    df_everyday = pd.DataFrame(everyday_conversations["messages"])
    df_topical = pd.DataFrame(topical_chat["content"])

    # Standardize column names
    df_everyday.rename(columns={"messages": "msgContents"}, inplace=True)
    df_topical.rename(columns={"content": "msgContents"}, inplace=True)

    # Reformat text (lowercase, remove extra whitespace)
    df_everyday["msgContents"] = df_everyday["msgContents"].apply(lambda x: [msg["content"].strip().lower() for msg in x])
    df_topical["msgContents"] = df_topical["msgContents"].apply(lambda x: [msg["message"].strip().lower() for msg in x])

    # Merge the datasets
    df_combined = pd.concat([df_everyday, df_topical], ignore_index=True)

    # Save as .csv
    df_combined.to_csv("processedDatasets.csv", index=False)

    print("Preprocessing complete! Saved as 'processedDatasets.csv'.")
