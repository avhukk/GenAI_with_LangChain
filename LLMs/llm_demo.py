import os 
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

# Load the key before starting to work with the model 
load_dotenv()

#Initialize the model 
model = ChatAnthropic(model = "claude-3-5-sonnet-20240620", temperature=0)


#Invoke the model 
response = model.invoke([
    HumanMessage(content="Explain how quantum computing is different from normal computing in two sentences")
])
print(response.content)

