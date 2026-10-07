from langchain_huggingface import HuggingFaceEmbeddings
import pandas as pd 

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
with open("output.txt", 'r', encoding= 'utf-8') as f:
    text = f.read()

documents = [text] 

vector = embedding.embed_documents(documents)
print(len(vector))
print(len(vector[0]))
