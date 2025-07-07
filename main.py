from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

print("Loaded key:", os.getenv("OPENAI_API_KEY")[:8] + "..." if os.getenv("OPENAI_API_KEY") else "NOT FOUND")

def main():
    model = ChatOpenAI(temperature = 0)

    tools = []

    agent_executor = create_react_agent(model, tools)

    print("Welcome to your AI assistant")
    print("You can tell me to do calculations")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()                    