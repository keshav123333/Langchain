# load bahut time leta hai toh uske liye lazy load karte hai matlab jab jarurat ho tabhi load karenge
# lazy load maan first page toh sirf first page ka content memory m load and baki ni then if line wise acess bhi toh ek page load then vo hata then jab dusra acess toh 
# load sari files pehle load then show isliye badi files ya directory toh ye use 

from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
loader=DirectoryLoader("lecture-12_document_loader/books",glob="**/*.pdf",loader_cls=PyPDFLoader)

doc=loader.lazy_load()

for i in doc:
    print(i[0])
