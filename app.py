from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os 
import streamlit as st
from dotenv import load_dotenv 
load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system","you are a ai assistant teacher"),
    ("user" , "question :{question}")
])

llm = ChatOpenAI()
outputparser = StrOutputParser()
chain = prompt|llm|outputparser

input_text = st.text_input("what is your question")

if input_text:
    st.write(chain.invoke({"question": input_text}))


