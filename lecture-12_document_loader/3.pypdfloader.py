from langchain_community.document_loaders import PyPDFLoader
# first

# pip install pypdf 

# ye generally har page ke content ko lata hai so doc[0]se page 0 and aise and ye un pdf ke liye acha jisnhe copy kar sakte if iage ya scanner toh ye badiya ni hai 
# usecase ke hisab se aise bahut se pdfloaders hai jaise unse text extract karna ya image extract karna ya table extract karna toh usecase ke hisab se alag alag loaders hai
loader=PyPDFLoader(file_path="lecture-12_document_loader/IoT Forensics Course Handout.pdf")
doc=loader.load()
print(doc[0].page_content)