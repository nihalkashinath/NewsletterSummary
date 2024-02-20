import os
import streamlit as st
from langchain_together import Together
from langchain import LLMChain, PromptTemplate
#from langchain_openai import ChatOpenAI
#from getpass import getpass


llama_model = Together(
    model="meta-llama/Llama-2-70b-chat-hf",
    # model = "mistralai/Mistral-7B-Instruct-v0.2",
    # model = "Qwen/Qwen1.5-72B-Chat",
    temperature=0.7,
)

newsletter_template = """
Provide the top {number} key news highlights from the following newsletter content: "{content}".
"""
#newsletter_content = input(prompt = 'Enter newsletter content here:')
newsletter_prompt = PromptTemplate(template = newsletter_template, input_variables = ['number', 'content'])

newsletter_chain = LLMChain(prompt = newsletter_prompt, llm = llama_model)

st.title("Newsletter Summarizer!")
st.subheader("🚀 Gets the key highlights from newletter content")

newsletter_content = st.text_input("Content:")

number_highlights = st.number_input("Number of highlights", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Summarize now!"):
    nl_highlights = newsletter_chain.run(number = number_highlights, content = newsletter_content)
    st.write(nl_highlights)

#print(newsletter_chain.run(number = 4, content = newsletter_content))

