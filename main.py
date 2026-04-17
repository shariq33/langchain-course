from dotenv import load_dotenv

load_dotenv()
import os


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("GEMINI_API_KEY"))
    print(os.environ.get("OLLAMA_API_KEY"))


if __name__ == "__main__":
    main()
