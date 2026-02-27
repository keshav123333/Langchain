from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
# pip install unstructured

loader = DirectoryLoader(
    "lecture-12_document_loader/books",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader   # 👈 VERY IMPORTANT yaha pe main pdf files sare soo
)
docs=loader.load()
print(docs[0].page_content)
print(len(docs))
# and sare pdf ek ke pages sum hoke aa gaye 
# ye sare pdf ko ek sath dega aur glob se humne ye specify kiya hai ki hume sare pdf chahiye jo us directory ke andar hai chahe wo kisi bhi subdirectory me ho toh glob ka use karke humne ye specify kiya hai ki hume sare pdf chahiye.





# PPT KE LIYE from langchain_community.document_loaders import DirectoryLoader, UnstructuredPowerPointLoader

# loader = DirectoryLoader(
#     "lecture-12_document_loader/ppt_folder",
#     glob="**/*.pptx",
#     loader_cls=UnstructuredPowerPointLoader
# )

# docs = loader.load()

# print(len(docs))



# IF EK DIRECTORY MEIN PDF TXT AND AUR BHI TOH YE USE 
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

# PDF files
pdf_loader = DirectoryLoader(
    "data",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

# TXT files
txt_loader = DirectoryLoader(
    "data",
    glob="**/*.txt",
    loader_cls=TextLoader
)

pdf_docs = pdf_loader.load()
txt_docs = txt_loader.load()

documents = pdf_docs + txt_docs

print(len(documents))
print(documents[0].page_content)