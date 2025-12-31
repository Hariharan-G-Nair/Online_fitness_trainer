from Groq_API_key import GROQ_API_KEY

import os
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"}
)


file_paths = [
    "1500_workout_routines.csv",
    "indian_nutrition_diet_1200_records.csv",
    "indian_food_nutrition_520_unique_foods.csv",
    "megaGymDataset.csv",
    "training_types.csv",
    "cardio_hiit_workouts_500_plus.csv",
    "workout_theory_nutrition_guide.csv",

]

documents = []

for path in file_paths:
    loader = CSVLoader(file_path = path,encoding = "utf-8")
    docs = loader.load()

    for doc in docs:
        doc.metadata["source_file"] = path
    documents.extend(docs)


vectorstore = FAISS.from_documents(documents,embeddings)

retriever = vectorstore.as_retriever(search_kwargs ={"k" : 3})


llm = ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature = 0.7
)


memory = ConversationBufferMemory(
    memory_key = "chat_history",
    return_messages = True
)


qa_chain = ConversationalRetrievalChain.from_llm(
    llm = llm,
    retriever = retriever,
    memory = memory,
    verbose = False
    
)



def ask_bot(question):
    result = qa_chain({"question": question})
    return result["answer"]