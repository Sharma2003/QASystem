import sys
from llama_index.core import SimpleDirectoryReader
from exception import customexception
from logger import logging


def load_data(data):
    """
    Load PDF documents from  a specificed directory

    Parameters:
    - data(str): The path to the directory conatining PDF files

    Returns:
    - A list of loaded PDF Documents. The specified type of documents may vary
    """

    try:
        logging.info("Data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("Data loading completed...")
        return documents
    
    except Exception as e:
        logging.info("Exception in loading data")
        return customexception(e,sys)