
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.runnables import RunnableParallel
#Plan of action 
# ek  text denge usse notes and quiz generate and uss note and quiz ko merge karwa de and final answer 
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=1.2)


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    max_new_tokens=100,
    temperature=0.7
)
model1=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template="generate short and simple notes from following text \n {text}",
    input_variables=['text']
)

prompt2=PromptTemplate(
    template="generate 5 sort question answer from following text \n {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="merge the rpovided notes and quiz into a single document \n notes {notes} and {quiz}",
    input_variables=['quiz','notes']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes': prompt1 | model | parser,
    "quiz" : prompt2 | model1 | parser
}) 
#upar wale mein ek text gaya jo invoke ke time gaya uss text se isne note and quiz nikala and usse then merge ke lye bhej diya 

merge_chain=prompt3 | model1 | parser

chain= parallel_chain | merge_chain

text=""""
Weather is the day-to-day state of the atmosphere, defined by components like temperature, humidity, wind, pressure, clouds, and precipitation. Driven primarily by the sun, it affects daily life, agriculture, and safety, ranging from sunny days to extreme events like storms and tornadoes. Key topics include forecasting, types, and impacts. 
Here is a breakdown of topics and subtopics related to weather:
1. Fundamentals of Weather
Definition & Basics: What is weather? (hourly/daily atmospheric conditions).
Key Elements: Temperature (hot/cold), humidity (moisture), atmospheric pressure, wind speed/direction, clouds, and precipitation.
Causes of Weather: The role of the sun, heat transfer, and air movement.
Air Masses & Fronts: How different air bodies interact to create changes. 
"""
result=chain.invoke({
'text':text
})

print(result)
chain.get_graph().print_ascii()

