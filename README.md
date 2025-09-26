## Design and Implementation of LangChain Expression Language (LCEL) Expressions

### AIM:
To design and implement a LangChain Expression Language (LCEL) expression using prompt, model, and output parser, and evaluate its functionality with multiple prompt parameters.

### DESIGN STEPS:

#### STEP 1:
Import necessary libraries (langchain, openai, dotenv).
#### STEP 2:
Define a prompt template with two parameters (concept, audience).
#### STEP 3:
Initialize the LLM model (ChatOpenAI).
#### STEP 4:
Use an output parser (StrOutputParser) for clean responses.
#### STEP 5:
Combine prompt, model, and parser into an LCEL chain and invoke with inputs.

### PROGRAM:
```python
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

```

### OUTPUT:
<img width="1830" height="282" alt="Screenshot 2025-09-26 101828" src="https://github.com/user-attachments/assets/b64f4271-a180-4df2-923b-a4635c9e309e" />


### RESULT:
Hence, the LCEL expression using LangChain with prompt, model, and output parser is successfully designed, implemented, and executed to generate context-specific explanations.
