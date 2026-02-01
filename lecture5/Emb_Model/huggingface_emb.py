from langchain_huggingface import HuggingFaceEmbeddings

emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="delhi is pollutated"

result=emb.embed_query(text)
print(str(result))

#if document hai toh

text=["delhi is pollutated","jaipur is capital of "]

result=emb.embed_documents(text)
print(len(str(result)))