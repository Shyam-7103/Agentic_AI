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
    input_variables=["player","match_situation","batsman_on_strike","bowler","stadium"],
    template="""
You are an AI assistant optimized to write professinol cricket commentary.
use persona prompt technique to write a professional cricket commentary <150 or 200 words about {player} in the {match_situation}.    
Batsman on strike: {batsman_on_strike}
Bowler: {bowler}
Stadium: {stadium}
"""
)

player = input("Player: ")
match_situation = input("Match Situation: ")
batsman_on_strike = input("Batsman on Strike: ")
bowler = input("Bowler: ")
stadium = input("Stadium: ")

final_prompt = prompt.format(
    player=player,
    match_situation=match_situation,
    batsman_on_strike=batsman_on_strike,
    bowler=bowler,
    stadium=stadium
)

response = llm.invoke(final_prompt)

print("\nGenerated Cricket Commentary:\n")
print(response.content)