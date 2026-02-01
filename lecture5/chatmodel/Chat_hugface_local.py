from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import os

# os.environ["HF_HOME"]="D:/huggingface"  -> ye code use  #so ab by default c drive ki jagah d drive mein yaha poe store model

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100
    }
)

model=ChatHuggingFace(llm=llm)

print(model.invoke("who is eldian in aot"))