from config import llm, prompt
from langchain_community.agent_toolkits import load_tools
from langchain.agents import AgentType, initialize_agent

# Load tools
tools = load_tools(["llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Use the ReAct agent type
    verbose=True,
)

# Invoke the agent
response = agent.invoke({"input": "What is 5**2?"})
print(response)
