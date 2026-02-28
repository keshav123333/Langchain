# pehli ssamjh isko like hum yaha pe kosis karte pehle para me tode \n\n -> \n line mein todne -> then word m toden -> then character m tod 
# matlab maan le chunck size 20 and ek do jisme pehle para m toda so ek para 20 se kam toh usse paura le liye ek para m 20 se jyda
# so usko lines m thoda lines m bhi jayda so usko  word m toda if word m todne se 20 se sam toh kuch word jod de then aise 20 size ke andar try

# main benfit ye try karta ki jitni limit usme ek para ya line aa jaye jisse context rahe if n aa paari toh lines and word m tod 

#  watch lecture 13 bahut aha hai chota sa recursvie text wala sec dekh le 

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load the text file
loader=TextLoader("lecture-13_textsplitter/1.Notes.txt")
doc=loader.lazy_load()

splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)

content=splitter.split_documents(doc)
print(content[0:2])
 
