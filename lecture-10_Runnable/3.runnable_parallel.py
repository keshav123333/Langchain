from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt=PromptTemplate(
    template="""create a linkdin post for this {topic}""",
    input_variables=['topic']

)

prompt1=PromptTemplate(
    template="""write a silly argument about this {topic}""",
    input_variables=['topic']

)

chain=RunnableParallel({
    'linkdin': prompt | model |  parser,
    'argument': prompt1 | model | parser
})

# ye ek dict return jisme linkdin and argument then vo aage wali chain mein as input jayenge ye chain dict dega ye yaad rakh

# samjh ye chain mein topic chain  wali runnable paralel dono chain ko mila,
# unhone ek text output diya jo lindin and argument mein save and dict ban gayi
# input jo dict m isse aage de bhi sakta jiase lecture 9 ke parallel wale m diya tha as a dict chain bana ke 

chain.invoke({
    "topic": "work life balance"
})
