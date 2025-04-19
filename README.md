Project for AI 481 
# GeneralChatbot chatbot 🤖

A **General Q&A Chatbot** built using **Chatterbot**, to provide intelligent responses. This chatbot learns from past interactions and fetches real-world knowledge when needed.


## 🚀 Features 
- **Conversational AI** powered by Chatbot
- **Real-time knowledge** fetching via **Wikipedia API**.
- Uses **Chatterbot's NLP alogrithms** for Q&A 
- Supports **predefined responses** and can learn dynamically 
- Stores conversation history using **SQL Storage Adapter** 
- Can be **trained with additional data** for better accuracy. 

## 🛠️ Technologies Used 
- **Python3** 
- **Chatterbot** (Ai-powered, NLP & response matching)
- **Chatterbot Corpus** (pre-trained responses) 
- **SQLite3** (for storing chat history)
- **spaCy** (optional for better NLP processing)
- **Wikipedia API** (for real-world knowledge)
- **Hugging Face Datasets** (for training on everyday conversation and deeper knowledge of more diverse topics)
- **Pandas** (for preprocessing the training data into a consistent format)

## 📌 Installation 
### 1. **Clone the Repository** 
```bash 
git clone https://github.com/Victoriaaguz/GeneralChatbot.git
cd qna-chatbot

```

### 2. Set up Virtual environment (Recommended)
``` bash 
python3 -m venv chatbot_env
source chatbot_env/bin/activate # for macOS/Linux
```

### 3. Install required dependcies 
```bash 
pip install chatterbot chatterbot_corpus sqlalchemy spacy wikipedia pandas datasets
pythons -m spacy download en_core_web_sm #(optional for NLP)
``` 
### Usage 
Run the chatbot by executing: 
```bash 
python3 Chatbot.py
```
Start chatting :) 



---

### **Created by:**
- **Victoriaaguz, michaelagarciaa, RapidCancel** 
- **Developed by Victoria Guzman, Michael Garcia, Andrew Ho**.
