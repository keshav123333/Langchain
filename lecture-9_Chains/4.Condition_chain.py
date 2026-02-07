
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from typing import Literal
from pydantic import BaseModel,Field
#Plan of action 
# isme hum pehle ek feedback if feedback postive toh kuch bhejte if negative toh kuch aur bhjenge 
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    max_new_tokens=100,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

class feedback(BaseModel):
    sentiment: Literal["postive","negaive"]=Field(description="Give the sentiment of the feedback")



parser=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=["feedback"],
    partial_variables={'format_instruction':parser2.get_format_instructions()}

)

classifier_chain=prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)


parser=StrOutputParser()

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='postive',prompt2 | model | parser),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment only fet this{x}")
)

chain=classifier_chain | branch_chain

print(chain.invoke({
    'feedback': "this is peice of shit"
}))

chain.get_graph().print_ascii()
