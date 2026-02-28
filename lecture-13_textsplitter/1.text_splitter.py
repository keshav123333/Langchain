from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load the text file
loader=TextLoader("lecture-13_textsplitter/1.Notes.txt")

doc=loader.load()

# Create a TextSplitter instance
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20,separator=" ") #chunk overlap is 20% of chunklen  #chunk overlap means 100 size ki len m batenge like 200 word ka txt so pehle 100 the
# jab dusre ko batenge toh 20 word pehle se overlap hogameans dusre m bhi 100 hi ayenge but pehle wale 100 m se 20 overlap honge as text bich se achnak se na ka jaye isliye 


content=text_splitter.split_documents(doc)
print(content[0:2])
