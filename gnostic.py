from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(tools=[DuckDuckGoTools()], markdown=True)
agent.print_response("Whats happening in France?", stream=True)