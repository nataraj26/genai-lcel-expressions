#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

# Step 1: Create prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {concept} in a way that a {audience} can understand."
)

# Step 2: Initialize the LLM
model = ChatOpenAI()

# Step 3: Initialize the output parser
parser = StrOutputParser()

# Step 4: Pass inputs through each component manually
formatted_prompt = prompt.format(concept="genAi", audience="beginner")
response = model.invoke(formatted_prompt)
final_output = parser.invoke(response)

print(final_output)

