from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

# YE USE JAB CONDIDTIO SE TUJHE EXECUTE KARWANA KUCHLIKE IF PEHI CONDTION TRUE TOH YE RUNNABLE IF DUSRI TOH DUSRA AND EK DEFAULT HOTI

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

#WORFLOW EK JOKE GENRATE IF VO JOKE 500 LEN SE BADI TOH SUMMARISE AND IF NI TOH VAISE HI
prompt1=PromptTemplate(template="""write a joke about {topic}""",input_variables=["topic"])
joke_gen=prompt1 | model | parser

prompt2=PromptTemplate(
    template="""summarise the following joke in less than 10 words {joke}""",
    input_variables=["joke"]
)

def word_count(text):
    return len(text.split())>500
# u can use lambda function bhi yaha pe but ye ek alag se function banake bhi use kar sakte ho
par=RunnableBranch(
    (word_count, prompt2 | model | parser), #so jo word isme input m jayega if word count 500 se bada toh ye wali chain excute varna default wala hi pass
    default=RunnablePassthrough()
)
chain=joke_gen | par

print(chain.invoke({"topic":"programming"}))