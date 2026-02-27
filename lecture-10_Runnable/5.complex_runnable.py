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
    template="""explain this joke {joke}""",
    input_variables=["joke"]
)


# ye joke text jo dono parallel ke andar ke key ko milegi ab joke toh usse vaise hi pass and joke key m save and explain usee
# pehle prmpt then model parser se pass then save 

par=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "explain":prompt2 | model | parser 
    }
)
prompt3=PromptTemplate(
    template="""summary of this explain {explain}""",
    input_variables=["explain"]
)

# sun meri baat ab digram dekh vo hi flow

chain1= joke_gen | par

par2=RunnableParallel({
    "joke_explain":RunnablePassthrough(),
    
    "summary": prompt3 | model | parser
})

# if tujhe sab alag joke explain summary toh chain1 ko invioke and usme se explain ko dict se le and aage bhej de 
chain2=chain1 | par2 

print(chain2.invoke({"topic":"india"}))



# NICHE WALA BHI SAME HI OUT KUCH NAYA NI 

# from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation",
#     temperature=0.7
# )

# model = ChatHuggingFace(llm=llm)
# parser = StrOutputParser()

# # 1️⃣ Joke Generator
# prompt1 = PromptTemplate(
#     template="write a joke about {topic}",
#     input_variables=["topic"]
# )

# joke_chain = prompt1 | model | parser


# # 2️⃣ Explanation Prompt
# prompt2 = PromptTemplate(
#     template="explain this joke: {joke}",
#     input_variables=["joke"]
# )


# # 3️⃣ Summary Prompt
# prompt3 = PromptTemplate(
#     template="give a short summary of this explanation: {explain}",
#     input_variables=["explain"]
# )


# # 🔥 Full Pipeline

# full_chain = (
#     joke_chain
#     | RunnableParallel({
#         "joke": RunnablePassthrough(),
#         "explain": prompt2 | model | parser
#     })
#     | RunnableParallel({
#         "joke": RunnablePassthrough(),
#         "explain": RunnablePassthrough(),
#         "summary": prompt3 | model | parser
#     })
# )

# result = full_chain.invoke({"topic": "India"})
# print(result)