from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)


parser=JsonOutputParser()

# template=PromptTemplate(
#     template="Give me name, age, and city of a fictional character \n {format_instruction}", # yaha pe format instrcution ek line add karwa deta ki reutrn in json in the prompt and out jisse json m 
#     input_variables=[],
#     partial_variables={"format_instruction": parser.get_format_instructions()}

# )

# pr=template.format()
# print(pr)
# # Output
# #Give me name, age, and city of a fictional character 
# #  Return a JSON object.

# result=model.invoke(pr)
# final_result=parser.parse(result.content)
# print(final_result)    # ye ab humara ek json format mein hoga

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #now same thing using chain

template=PromptTemplate(
    template="Give me name, age, and city of a fictional character {marks} \n {format_instruction}", # yaha pe format instrcution ek line add karwa deta ki reutrn in json in the prompt and out jisse json m 
    input_variables=["marks"],
    partial_variables={"format_instruction": parser.get_format_instructions()}

)

chain=template | model | parser #last mein parser se so json m out mile

result=chain.invoke({"marks":"21"})
print(result)