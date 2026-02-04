from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from typing import Optional,Literal

model=ChatOpenAI()

class Review(BaseModel):
    key_theme=list[str]=Field(description="Write down all the theme discussed in the review ")
    summary:str=Field(description="A beirf summary of the review")
    sentiment:Literal["pos","neg"]=Field(description="Write sentiment analysis of the review")
    pros:Optional[list[str]]=Field(description="write positve thing about the review in this section give postive news of the prod")
    cons:Optional[list[str]]=Field(description="Write down the negative thing about review in this list format")
    name:Optional[str]=Field(description="wrtie the name of the reviewer")


structured_model=model.with_structured_output(Review,method="json_mode")  #for open ai function_calling' method m jayega and for gemini clude json bhi 

result=structured_model.invoke("""The realme 11x 5G (approx. ₹14,999) is a budget 5G phone, praised for its 64MP camera, 120Hz display, and 33W fast charging, making it a solid daily driver. While featuring a unique design and good battery life, users report a heavily pre-installed software (bloatware) and average low-light camera performance. 
This video""")
   
print(result)


