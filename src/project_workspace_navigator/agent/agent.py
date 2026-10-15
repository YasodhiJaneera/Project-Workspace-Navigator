from pydantic_ai import Agent
import os
from dotenv import load_dotenv


load_dotenv()


agent = Agent(
    os.environ["GROQ_AGENT_LLM"]
)
print(agent.run_sync("Hi")) 