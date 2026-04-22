from dotenv import load_dotenv
load_dotenv()
import os

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()



tavily_key = os.getenv("TAVILY_API_KEY")
print(tavily_key)
tavily = TavilyClient(api_key=tavily_key)

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    return tavily.search(query=query, max_results=2)


#llm = ChatOpenAI(model="gpt-5")
llm = ChatOllama(temperature=0, model="mistral:latest")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()