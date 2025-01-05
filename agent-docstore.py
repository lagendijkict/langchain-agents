from config import hub_prompt, llm
from langchain import Wikipedia
from langchain.agents import Tool
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain.agents.react.base import DocstoreExplorer


docstore = DocstoreExplorer(Wikipedia())
tools = [
    Tool(name="Search", func=docstore.search, description="search wikipedia"),
    Tool(name="Lookup", func=docstore.lookup, description="lookup a term in wikipedia"),
]

agent = create_react_agent(llm=llm, tools=tools, prompt=hub_prompt)
# Wrap the agent in an executor
agent_executor_sql = AgentExecutor(
    agent=agent, tools=tools, verbose=True, max_iterations=3, handle_parsing_errors=True
)

# Invoke the agent with a docstore question
agent_executor_sql.invoke({"input": "What is the capital of Austria?"})
