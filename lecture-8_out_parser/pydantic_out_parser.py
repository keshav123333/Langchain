from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
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


class Person(BaseModel):
    name: str=Field(description="write name or product")
    age: int =Field(gt=18,description="write down the age of the person that is from this para")
    city: str=Field(description="name of the city the person belongs to ")


parser=PydanticOutputParser(pydantic_object=Person)


template=PromptTemplate(
    template="Generate the name ,age of city of a fictional {place} person\n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

# prompt=template.invoke({'place':'indian'})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)


# upar ka same kaam simple do teen line m

chain=template | model | parser
final_result=chain.invoke({'place':'sri-lanka'})

print(final_result)