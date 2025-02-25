Project for AI 481 
# GeneralChatbot Q&A chatbot 🤖

A **General Q&A Chatbot** built using **Chatterbot**, a machine learning based conversational chatbot libray. This chatbot can answer general questions, learn from past interactions, and improve over time.

## 🚀 Features 
- Uses **Chatterbot's NLP alogrithms** for Q&A 
- Supports **predefined responses** and can learn dynamically 
- Stores conversation history using **SQL Storage Adapter** 
- Can be **trained with additional data** for better accuracy. 

## 🛠️ Technologies Used 
- **Python3** 
- **Chatterbot** (NLP & response matching)
- **Chatterbot Corpus** (pre-trained responses) 
- **SQLlite** (for storing chat history)
- **spaCy** (optional for better NLP processing)

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
pip intall chatterbot chatterbot_corpus sqlachemy spacy
pythons -m spacy download en_core_web_sm #(optional for NLP)
``` 
### Usage 
Run the chatbot by executing: 
```bash 
python3 Chatbot.py
```
Start chating :) 



---

### **Created by:**
- **Victoriaaguz & michaelagarciaa** 
- **Developed by Victoria Guzman & Michael Garcia**.
