from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    
    temperature=0.8
)

model=ChatHuggingFace(llm=llm)


 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>_______________________________________________>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#basic chatbot 


# chat=[]

# while True:
#     user_input=input("You : ")
#     if user_input=='exit' or user_input=='':
#         break

#     chat.append(user_input)

#     result=model.invoke(chat)
#     chat.append(result.content)
#     print(result.content)



# --------------------------------------------------------------------------------------------------------------------


# Main problem in this is that precisely ni kaha sakte ki kaunsa kiska reply and bhaut bada bhi ho jayega 

# langchain hv three type of msg system msg human msg ai msg 

# # system msg : conversation ki satrt m jata like tu ek acha chatbpt hai like behave like a choild type thing
# human msg -: human msg jo behjta 
# ai msg : ye ai bhejta hai


# from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# chat=[
#     SystemMessage(content="You Are Helpful Ai Assistant")
# ]

# while True:
#     user_input=input("You : ")
#     chat.append(HumanMessage(content=user_input))
#     if user_input=='exit':
#         break
#     result=model.invoke(chat)
#     chat.append(AIMessage(content=result.content))
#     print("AI :", result.content)
    

#----------------------------------------------------------------------------------------------------------------


# # ab humne dekha ki like maan le pehle model.invoke mein kitne tarah se bhej sakte hai msg
# # 1. way direct invok mein string likh di 
# # 2. Dynamic msg bheja jisme Prompt template use kiya har baar diff
# # 3. List of msg bheje jsime human ai system 
# # 4. ab ye list of msg ko dynamic bana sakte hai kya hum ye quesion 


# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# chat_temp=ChatPromptTemplate([
#     ('system','You are a helpful {domain} expert'),
#     ('human','Explain in simple terms, what is {topic}')
# ])

# prompt=chat_temp.invoke({
#     'domain':'cricket', # ye crikcket ye sab tu dynamically user se bhi le sakta hai so yaha toh maine likh diya but input se le sakta hai tu chahe toh

#     'topic':'Dusra'
# })


# print(prompt)

# # aisa ek template pass ho jayega
# # output -:
# # messages=[SystemMessage(content='You are a helpful cricket expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is Dusra', additional_kwargs={}, response_metadata={})] 



#------------------------------------------------------------------------------------------------------------------------------------

# maan le ek bande ne pehle ek chat ki ab vo kuch dino baad fir aake chat ke toh ab usko kahi save karna hoga na so jisse kuch dino baad aaye toh vo chat de sake 

# so hum chat_hist.txt m pehle ki chat usse vapis lenge 


from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage

chat_template=ChatPromptTemplate([
    ('system','you are a helpful agent'),
    MessagesPlaceholder(variable_name='chat-history'),
    ('human','{query}'),
    ('ai','{aimsg}')
])

history=[]

with open('lecture-6/chat_hist.txt') as f:
    history.extend(f.readlines())

print('Start')
print(history)

prompt=chat_template.invoke({'chat-history':history,'query':'where is my refund','aimsg':'hello'})
history.extend(prompt)

print(prompt)