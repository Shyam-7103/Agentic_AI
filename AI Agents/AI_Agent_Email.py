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
    input_variables=["content", "customer_name", "agent_name"],
    template="""
You are an AI assistant optimized to write concise, professional, and friendly emails.

Write a professional email to {customer_name}.

Content:
{content}

Signature:
{agent_name}
"""
)

content = input("Email content: ")
customer = input("Customer name: ")
agent = input("Agent name: ")

final_prompt = prompt.format(
    content=content,
    customer_name=customer,
    agent_name=agent
)

response = llm.invoke(final_prompt)

print("\nGenerated Email:\n")
print(response.content)