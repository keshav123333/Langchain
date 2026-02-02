from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint  #yaha pe tu chahe toh chagpt ki api bhi use 
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    temperature=0.8
)

model=ChatHuggingFace(llm=llm)




# THIS IS THE FIRST STEP 
# st.header("Research Purpose")

# paper_input=st.selectbox("Select Research Paper Name",[])

# user_input=st.text_input("Enter ur Prompt")

# if st.button('Summarize'):
#     result=model.invoke(user_input)
#     st.write(result.content)




#################################################################3

# 2ND ISKO AUR FURNISH KARA HUMNE

# st.header("Research Paper")

# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
# user_inp=st.text_input("Enter something More you want")

# template=PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:

# Explanation Style: {style_input}
# Explanation Length: {length_input}

# Also Keep this in mind : {user_input}

# 1. Mathematical Details:

# Include relevant mathematical equations if present in the paper.

# Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:

# Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

# Ensure the summary is clear, accurate, and aligned with the provided style and length.


# """,
# input_variables=['paper_input','style_input','length_input','user_input'], #ye bata raha ki variable kya,
# validate_template= True  #ye validate ki input variable pure ya ni if input varible mein ek zayda kam add toh ye error on develpoer side 

# )


# prompt=template.invoke({
#     'paper_input':paper_input
#     ,
#     'style_input': style_input
#     ,'length_input':length_input,
#     'user_input':user_inp
# })

# if st.button("Summarize"):
#     st.write(model.invoke(prompt).content)







####################################################################

#3rd same bad ab humne template ko json mein daal diya ab usse input load karke use karenge

# st.header("Research Paper")

# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template=load_prompt("lecture-6/template.json")


# prompt=template.invoke({
#     'paper_input':paper_input
#     ,
#     'style_input': style_input
#     ,'length_input':length_input
# })

# if st.button("Summarize"):
#     st.write(model.invoke(prompt).content)













#####################################3333
#4 th chain bana ke use baar baar invoke kyon ek baar kyon nist.header("Research Paper")
# st.header("Research Paper")
# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template=load_prompt("lecture-6/template.json")


 

# if st.button("Summarize"):
#     chain=template | model  #model and template ki chain bana di
#     result=chain.invoke({
#      'paper_input':paper_input
#      ,
#      'style_input': style_input
#      ,'length_input':length_input
#     })
#     st.write(result.content)


