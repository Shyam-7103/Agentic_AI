from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.0
)

prompt = PromptTemplate(
    input_variables=["topic", "tone", "target_audience"],
    template="""
You are an AI Agent to write professional linkedin posts.

Write a professional linkedin post about {topic}.

Tone: {tone}

Target Audience: {target_audience}
""" 
)

topic = input("Topic: ")
tone = input("Tone: ")
target_audience = input("Target Audience: ")

final_prompt = prompt.format(
    topic=topic,
    tone=tone,
    target_audience=target_audience
)

response = llm.invoke(final_prompt)

print("\nGenerated LinkedIn Post:\n")
print(response.content)