import os
from crewai import Agent, LLM
from dotenv import load_dotenv

# Load variables from your .env file
load_dotenv()

# Initialize the verified Groq Production Model
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",        
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.7,
    max_tokens=1024,
)

# Quick background terminal check to verify connectivity when app starts
if os.environ.get("GROQ_API_KEY"):
    print("🚀 [Groq Config] API Key found. Connecting to llama-3.1-8b-instant...")
else:
    print("⚠️ [Groq Config] WARNING: GROQ_API_KEY is missing from your .env file!")


def content_researcher():
    return Agent(
        role="Content Researcher",
        goal="Research trending and valuable information about the given topic.",
        backstory="You are an expert internet researcher who finds concise, useful and engaging insights quickly.",
        llm=groq_llm,
        verbose=False
    )


def content_writer():
    return Agent(
        role="Content Writer",
        goal="Create high-quality content in multiple formats.",
        backstory="You are a professional writer skilled in blogs, emails, captions, LinkedIn posts and scripts.",
        llm=groq_llm,
        verbose=False
    )