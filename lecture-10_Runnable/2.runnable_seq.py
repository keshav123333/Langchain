from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt=PromptTemplate(
    template="""tell me a joke about {topic}""",
    input_variables=['topic']

)

prompt1=PromptTemplate(
    template="""explain me this joke {text}""",
    input_variables=['text']

)

chain=prompt | model | parser | prompt1 | model | parser

print(chain.invoke({
    "topic":"ai"
}))