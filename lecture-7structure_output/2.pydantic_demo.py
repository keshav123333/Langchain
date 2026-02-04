from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str ='bitish ' #defualt bhi daal sakte 
    age: Optional[int]=None
    email: EmailStr #ye tai karega ki ismejo pass vo ek email ho
    cgpa: float=Field(gt=0,lt=10,default=5,description="a decimal value b/w 0 to 10")


new_student={'name':'nitish','email':'esha@gmail.com','cgpa':9.99}

student=Student(**new_student)

student_dict=dict(student)
student_json=student.model_dump_json

print(student_dict["name"])
print(student_json)