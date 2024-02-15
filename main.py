import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain import LLMChain, PromptTemplate

os.environ["OPENAI_API_KEY"] = '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'

# st.secrets["OPENAI_API_KEY"]

tweet_template = """
Give me {number} tweets on {topic}.
"""

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")  # use "gpt-4-0125-preview" for GPT-4 model

tweet_generator = LLMChain(prompt = tweet_prompt, llm = gpt3_model)

st.title("Tweet Generator 🐦")
st.subheader("🚀 Generate tweets on any topic")

user_topic = st.text_input("Topic")

user_number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_generator.run(number = user_number, topic = user_topic)
    st.write(tweets)
    # for tweet in tweets:
    #     st.write(tweet)