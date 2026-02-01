from langchain_antropic import ChatAntropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAntropic(model="claude-sonnet-4-5-20250929")

result=model.invoke("who was president of india")
print(result)
print(result.content)