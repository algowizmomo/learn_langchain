import os
import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama



prompt = ChatPromptTemplate.from_messages([("system","you are an ai assistant teacher for LKG students"),
                                           ("user","question : {question}")
                                           ])

llm = Ollama()
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

st.title("simple chatbot with ollama")
input_text = st.text_input("enter your question here: ")

if input_text:
    st.write(chain.invoke({"question": input_text}))