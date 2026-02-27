from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough

load_dotenv()


# RUNNABLE PASSTRHOUGH PASS HE AS ITIS VALUE IF A TEXT INP THAT SAME WILL BE OUT IF DICT IS THE INPUT IN IT A DICT 
# WILL COME AS OUT NO CHANGE


#  iska arch prompt1jokegen-> ye ek parallel seq mjo ek joke de de -> dusra joke ka explation

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

# ye ek joke text gen 

prompt2=PromptTemplate(
    template="""explain this joke {topic}""",
    input_variables=["topic"]
)


# ye joke text jo dono parallel ke andar ke key ko milegi ab joke toh usse vaise hi pass and joke key m save and explain usee
# pehle prmpt then model parser se pass then save 

par=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "expalin":prompt2 | model | parser 
    }
)

chain = joke_gen | par

print(chain.invoke({"topic":"BJP GOverment"}))
