from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #load the open ai api

llm=OpenAI(model="gpt-3.5-turbo-instruct")  #yaha pe model ko dekha maine llm mein maine store kiya 
result= llm.invoke("what is capital of india")  #then yaha pe llm ko invoke karke jawab mangwaya
print(result)