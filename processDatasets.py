# ===================================================================================
# NOTE: This file will load two datasets, preprocess and merge them into a .csv file
# If you want to add more datasets using the load_dataset() function, edit here
# ===================================================================================
from datasets import load_dataset
import pandas as pd

def process_datasets():
    # Corrected splits
    everyday_conversations = load_dataset("HuggingFaceTB/everyday-conversations-llama3.1-2k", split="train_sft")
    topical_chat = load_dataset("Conversational-Reasoning/Topical-Chat", split="train")

    # Convert to DataFrames
    df_everyday = pd.DataFrame(everyday_conversations)
    df_topical = pd.DataFrame(topical_chat)

    # Extract and clean 'messages'
    df_everyday["msgContents"] = df_everyday["messages"].apply(
        lambda x: [msg["content"].strip().lower() for msg in x]
    )
    
    df_topical["msgContents"] = df_topical["content"].apply(
        lambda x: [msg["message"].strip().lower() for msg in x]
    )


    # Keep only the cleaned columns
    df_everyday = df_everyday[["msgContents"]]
    df_topical = df_topical[["msgContents"]]

    # Merge both
    df_combined = pd.concat([df_everyday, df_topical], ignore_index=True)

    # Save to CSV
    df_combined.to_csv("processedDatasets.csv", index=False)
    df_everyday.to_csv("processedDatasets.csv", index=False)
    print("✅ Preprocessing complete! Saved as 'processedDatasets.csv'.")
