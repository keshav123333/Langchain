from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    max_new_tokens=100,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

result = model.invoke("hello hi how are you")
print(result.content)


#ye dusra tarika hai like isme hum model ke aage get api karke option aata usse karte bona langchain ke ye bhi ek way  
 

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)