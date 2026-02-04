# structured output agents mein zaruri means ll chatgpt se jab sawal pcta hai toh vo unstructred output deta tujhe haina ab tujhe vo unstructred ni chaiye tujhe proper  structred out lik json format like if place toh delhi ek proper time money value extract karke 
# structred out iske do ways hai 
# 1. with structred karke jo models hote unhe use kar 
# 2. unstructred out kisi bhi model ke out ko structred bana le 
# Ai Agents mein bhi bahut kaam aata hai ye as maan le tujhe ek text mein se paa karna ki user ne time kya bataya 


# this is how to create typed dic

from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_per:Person={'name':'keshav','age':12}

print(new_per)


#------------------------------------------------------------------------------------------------------------------------------------------------------

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# model=ChatOpenAI()

# class Review(TypedDict):
#     summary:str
#     sentiment:str


# structured_model=model.with_structured_output(Review)

# result=structured_model.invoke("""
# this is my name why this product sucks yaar i hate thsi 
# """)


# print(result["summary"])
# print(result)
#ab ye ek dict return jisme se fetch kar sakte ho jankari 



#------------------------------------------------------------------------------------------
# yaha pe prper method batayega kaise kya karna hai uska 

from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from typing import TypedDict,Annotated,Optional,Literal
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    max_new_tokens=100,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

#  ab like main chahu toh typed dict ke sath aur kuch kar sakt ahu
# meri baat sun ye jo typeddict model se invoke se laa sab 



##----------------->MOST IMP ye sirf open ai ke sath work arta hia mostly

class Review(TypedDict):
    key_themes:Annotated[list[str],"write down all key themes discussed in review give in a list"]
    summary: Annotated[str,"A brief summary of review"] #annotated jo hai ye like batane ke liye ki summary jo hai vo ya lena chata hai
    sentiment: Annotated[Literal["pos","neg"],"return sentiment of the review eith postive or neg or neutral"]
    #yaha pe maine dekh litral diya so means ye padega and ya toh pos ya neg in dono mein se hi return snetiment mein pehle str toh vo str deta kuch but ab ya pos ya neg
    pros:Annotated[Optional[list[str]],"Write all ebnfits or pros of in a list"]
# optional means ye pros jaruri ni hoga but if ayeg oth list format mein hoga 

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""The realme 11x 5G (approx. ₹14,999) is a budget 5G phone, praised for its 64MP camera, 120Hz display, and 33W fast charging, making it a solid daily driver. While featuring a unique design and good battery life, users report a heavily pre-installed software (bloatware) and average low-light camera performance. 
This video""")
   

print(result)