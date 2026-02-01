from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv() #dot env ko load

llm=ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=10)  # isko kam if more deteministic and fix 1 se bads if more random or creative jawab chaiye toh ye 0 se 2 ke bich
result=llm.invoke("hii hello")

print(result) #ye pura content ko print karega 
print(result.content) # ye result ke andar ke content ko bhi download 
