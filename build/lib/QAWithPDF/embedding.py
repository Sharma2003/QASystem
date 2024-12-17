import sys
from exception import customexception
from logger import logging
from llama_index.core import VectorStoreIndex, ServiceContext, StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

def download_gemini_embedding(model,document):
    """
    Downnload and initilizes a Gemini Embedding model for vector embedding 

    Return: 
     - VectorStorIndex: An index of vector embeddings for efficient  
    """