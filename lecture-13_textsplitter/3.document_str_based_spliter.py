from langchain_text_splitters import RecursiveCharacterTextSplitter,Language 

#ye used to split code and all and send it to out model
# ye class then function ke basis pe try karti seprate karne ka jaise pehle para tha so class then functon then para ke basis thn line ke basis pe seprate karte 

text= """
class Calculator:
    

    def __init__(self, a, b):
        
        self.a = a
        self.b = b

    def add(self):
        
        #Performs addition of the two numbers.
        
        return self.a + self.b

    def subtract(self):
         
        return self.a - self.b

    def multiply(self):
        
        return self.a * self.b

 
num1 = 10
num2 = 5
calculator_instance = Calculator(num1, num2)
 
print(f"Numbers: {num1}, {num2}")
print(f"Sum: {calculator_instance.add()}")
print(f"Subtraction: {calculator_instance.subtract()}")
print(f"Multiplication: {calculator_instance.multiply()}")

"""

splitter=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,chunk_size=150,chunk_overlap=20) #language=Language.MARKDOWN if like markdown m hai markdown means chagpt like para bold in sab m likhta check internet 

content=splitter.split_text(text=text)

print(content[1])