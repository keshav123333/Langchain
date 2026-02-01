from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",  max_output_tokens=10,temperature=1.2)

result=model.invoke("whi is pm of india iam keshav now iam prime inister of india")

print(result)
