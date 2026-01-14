from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model= "llama3.2")

template = """ You are answering reviews about an resturant.

Here are some reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate(template)
