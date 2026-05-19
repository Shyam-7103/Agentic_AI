from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

def write_email(topic: str) -> str:
    """Write a simple professional email based on the topic."""
    return f"""
Subject: {topic}

Dear Sir/Madam,

I hope you are doing well.

I am writing regarding {topic}. Please let me know if any further details are required.

Thank you.

Regards,
Shyam
"""

def daily_update(work: str) -> str:
    """Create a short internship daily update."""
    return f"""
Today's Work Update:

Today I worked on {work}.
I understood the basic flow and improved my practical implementation skills.

Regards,
Shyam
"""

def explain_concept(concept: str) -> str:
    """Explain a technical concept in beginner-friendly language."""
    return f"""
{concept} means understanding the topic step by step in a simple way.
It is useful in real projects because it helps us solve problems clearly.
"""

agent = create_agent(
    model=llm,
    tools=[write_email, daily_update, explain_concept],
    system_prompt="""
You are an AI Intern Assistant Agent.

Your job is to help an intern with:
1. Writing professional emails
2. Preparing daily work updates
3. Explaining technical concepts simply
4. Helping with basic office/internship tasks

Always answer in simple beginner-friendly language.
Use tools when needed.
"""
)

while True:
    user_input = input("\nAsk your AI Intern Agent: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Agent stopped.")
        break

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    print("\nAgent Response:")
    print(response["messages"][-1].content)