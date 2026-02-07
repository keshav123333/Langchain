#so sun jaise maine bataya ki with structred out format sirf chat gpt and gemini kuch ke sath kAAM KRTA BUT LIKE HUGGING FACE LLMAA MODEL KE SATH UNHE WORK KARWANE KE LIYE YE USE 
# 4 type ke pareser hote hai 
# 1. string output parser   

# so string parser kaha use vo deknge 


from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

#now ek model jisme ek topic dega vo uss topic ke summmary then vo summary vapis model mein jayegi and new 5 line summary ayegi

template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="Write a 5 line summary fot this {text}",
    input_variables=['text']
)
pr1=template1.invoke({'topic':'black rock'})
result1=model.invoke(pr1)

pr2=template2.invoke({
    'text':result1.content
})

result2=model.invoke(pr2)

print(result2)



#>>>>>>>>>----------------------------------------------------------------------------------------------------------------

#ye same kaam hum chain ki help se kar sakte so isko karne mein string parser help karta hai chain bana ke 

from langchain_core.output_parsers import StrOutputParser

parser=StrOutputParser()

chain=template1 | model | parser  | template2 | model | parser  #yaha pe parser vo hi kaam jo rsult.content karta content ko lata result se so chain mein result.content ni kar sakte so usko solve ke liye 

print(chain.invoke({'topic':'black-hole'}))
