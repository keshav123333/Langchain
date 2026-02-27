from langchain_community.document_loaders import UnstructuredPowerPointLoader
# first 
# pip install "unstructured[pptx]"
loader = UnstructuredPowerPointLoader(
    "lecture-12_document_loader/sample.pptx"
)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
#  aur bhi ways and loader hote hai
