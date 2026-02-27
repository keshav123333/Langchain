from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

# MAAN EK DATA USSE PEHLE PREPROCESS KARNA CAPITAL YA KUCH MARKS HATNA YA KUCH BHI NO. OF WORDS COUNT KARNA SO ISKE LIYE 
#  PIPLINE KE BICH M ADD KARNI PADEGI PYTHON KI FUNC ISKA FLOW DEKH DRAWIO MEIN
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="""write a joke about {topic}""",
    input_variables=["topic"]
)

joke_gen=prompt1 | model | parser

# par=RunnableParallel(
#     {
#         "joke":RunnablePassthrough(),
#         "joke_len":RunnableLambda(lambda x : len(x.split()))
#     }
# )
# yaha toh upar wala use vo fast

def wordcount(text):
    
    return len(text.split())

par=par=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "joke_len":RunnableLambda(wordcount)
    }
)