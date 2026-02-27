from langchain_community.document_loaders import WebBaseLoader
# isme list of url bhi de sakte hai 
loader=WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")

doc=loader.load()

print(doc[0].page_content)

# isse content ko prompt m bej ke sawal bhi puch sakta hai

# limitation that javascript heavy web site ni 

from langchain_community.document_loaders import SeleniumURLLoader
# first
# pip install selenium
# pip install webdriver-manager




# isko use tu chagpt se sikha le 

 