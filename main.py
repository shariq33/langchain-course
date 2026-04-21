from dotenv import load_dotenv

load_dotenv()
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
