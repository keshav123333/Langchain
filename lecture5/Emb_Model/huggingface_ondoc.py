from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#yaha pe open ai bhi use kar sakta same way se lecture 5 dekh sakta hai tu
emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document=[

"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
"Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
"Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."]

query="Who is a good bowler"

docemb=emb.embed_documents(document)
qemb=emb.embed_query(query)

score=cosine_similarity([qemb],docemb)
index=np.argmax(score)
print(score)
print(document[index])
