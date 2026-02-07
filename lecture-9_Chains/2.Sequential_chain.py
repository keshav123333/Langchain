# sequential chain banyenge 
# 1. topic -> llm -> report -> llm -> summary

from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


prompt1=PromptTemplate(
    template="generate detail report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="generate a 5 pointer summary for following {'text}",
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    max_new_tokens=100,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()
chain=prompt1 | model | parser | prompt2 | model | parser

chain.invoke({
    'topic':'unemployment in india'
})

chain.get_graph().print_ascii()