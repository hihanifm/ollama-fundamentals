import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return "It is always sunny here"


llm = ChatOpenAI(
    base_url=os.getenv("LM_STUDIO_BASE_URL"),
    api_key=os.getenv("LM_STUDIO_API_KEY"),
    model=os.getenv("LM_STUDIO_MODEL"),
)

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful AI assistant.",
)

response = agent.invoke({"messages": [{"role": "user", "content": "What is the weather in SFO?"}]})

for msg in response["messages"]:
    print(f"{msg.type}: {msg.content}")