from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

emb=OpenAIEmbeddings(model="ext-embedding-3-large",dimensions=32) #kitne ka vector out chaiye isse apne hisab se change bhi kar sakt like if 1024 ya usse zayada iska check ki max kitne dim ka le sakta hai tu 

result=emb.embed_query("Delhi pollution is high")
print(str(result))


#if ek sath more query toh 
# document=["delhi is captial ",
#           "jaipur is the city in ",
#           "hello mary how are you "]

# emb=OpenAIEmbeddings(model="ext-embedding-3-large",dimensions=32) #kitne ka vector out chaiye isse apne hisab se change bhi kar sakt like if 1024 ya usse zayada iska check ki max kitne dim ka le sakta hai tu 

# result=emb.embed_documents(document)
# print(str(result))

# result is 2d matrix jisme 3 matrix hogi