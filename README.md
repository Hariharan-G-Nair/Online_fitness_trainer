# AI Fitness Trainer — Retrieval-Augmented Generation (RAG) Chatbot with Llama 3


Fitness Trainer Chatbot is a conversational Retrieval-Augmented Generation (RAG) system built using Flask, LangChain, and Groq-hosted Llama 3.
The application answers fitness, workout, and nutrition-related queries by retrieving relevant information from a structured CSV knowledge base and generating accurate, context-aware responses using a large language model.

Unlike traditional chatbots that rely solely on pre-trained knowledge, this system dynamically retrieves domain-specific data using FAISS vector search, injects the retrieved context into the LLM prompt, and maintains conversation history to deliver coherent, multi-turn interactions.
This project demonstrates a practical, end-to-end implementation of a production-style RAG pipeline with a clean web interface and real-world applicability.

### 🚀 Features

📄 CSV-based knowledge source

🧠 Conversational memory (context-aware responses)

🔍 Semantic search using FAISS

🤖 Groq Llama 3 (8B) LLM

🌐 Flask REST API

💬 Simple browser-based Chat UI

⚡ Fast inference using Groq API




## 🏗️ Tech Stack

Backend: Flask

LLM: Groq – llama3-8b-8192

Framework: LangChain

Vector Store: FAISS

Embeddings: sentence-transformers/all-MiniLM-L6-v2

Frontend: HTML, CSS, Vanilla JavaScript

Language: Python 3.11




## 📁 Project Structure
Fitness_trainer_app/
│
├── app.py                 # Flask server
├── chatbot.py             # LangChain chatbot logic
├── data.csv               # Fitness knowledge base
├── Groq_API_key.py        # Groq API key file
├── requirements.txt
└── templates/
    └── index.html         # Chat UI




## 🔑 Prerequisites

Python 3.11

A Groq API Key
Get one from: https://console.groq.com



## ⚙️ Setup Instructions:

1️⃣ Clone the repository
git clone https://github.com/your-username/fitness-trainer-chatbot.git
cd fitness-trainer-chatbot

2️⃣ Create & activate virtual environment

Windows (PowerShell):

python -m venv myenv
myenv\Scripts\Activate.ps1

Windows (CMD):

python -m venv myenv
myenv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add Groq API Key

Create a file named Groq_API_key.py:

GROQ_API_KEY = "your_groq_api_key_here"

5️⃣ Run the application
python app.py

Open your browser:

http://127.0.0.1:5000


## ⚠️ Notes

FAISS index is rebuilt on app start

Memory resets when server restarts

First run may be slow due to embedding model download

favicon.ico 404 is normal and harmless


## 🔮 Future Improvements

💾 Persist FAISS index to disk

🧠 Per-user session memory

⏳ Streaming responses

🌙 Dark mode UI

🐳 Docker support

📱 Mobile-friendly UI


## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.


## 📜 License

This project is licensed under the MIT License.


## 👨‍💻 Author

Hariharan G
Data Scientist | Fitness  | AI Developer



