#Chains ka use karke aap EK PIPELINE BANATE JISSE PEHLA STEP EXECUTE THEN VAHA SE OUT JO AGLE STEP KE LIYE INPUT
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
prompt=PromptTemplate(
    template="Generate 5 intresting facts about {topic}",
    input_variables=["topic"]
              
)
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    max_new_tokens=100,
    temperature=0.7
)
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()
chain=prompt | model | parser
chain.get_graph().print_ascii()


