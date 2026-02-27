# do this to install the langchain-community package which has the TextLoader class
# pip install -U langchain-community   
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

load_dotenv()

 

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt1=PromptTemplate(template="""expalin what written in this \n {topic}""",input_variables=["topic"])

explain=prompt1 | model | parser
loader=TextLoader("lecture-12_document_loader/1.notes.txt", encoding="utf-8")
docs=loader.load()
# isme pagecontent and metdata and docs[0] se tu acces data and doc[0].pagecontent se tu page content ko access kar sakta hai
print(explain.invoke({"topic":docs[0].page_content}))

