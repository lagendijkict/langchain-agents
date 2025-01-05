from config import llm, hub_prompt, llm_chain_tool, sql_prompt
from sql_tool import sqlite_tool

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain.memory import ConversationBufferMemory  # Import memory class

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Load tools
tools = load_tools(["llm-math"], llm=llm)

# Create the agent
# agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# Wrap the agent in an executor
# agent_executor = AgentExecutor(
#     agent=agent, tools=tools, max_iterations=3, handle_parsing_errors=True
# )

# Invoke the agent with a math question
# response = agent_executor.invoke(
#     {
#         "input": """if Mary has four apples and Giorgio brings two and a half apple
#         boxes (apple box contains eight apples), how many apples do we have?"""
#     }
# )
# print(response)

tools.append(llm_chain_tool)
# agent_with_chain = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# Wrap the agent in an executor
# agent_executor = AgentExecutor(
#     agent=agent_with_chain,
#     tools=tools,
#     verbose=True,
#     max_iterations=3,
#     handle_parsing_errors=True,
# )
# Invoke the agent with a general question
# response_with_chain = agent_executor.invoke(
#     {
#         "input": """what is the median salary
#         of data scientists in the Netherlands in 2021?"""
#     }
# )

tools.append(sqlite_tool)
agent_with_sql = create_react_agent(llm=llm, tools=tools, prompt=sql_prompt)

# Wrap the agent in an executor
agent_executor_sql = AgentExecutor(
    agent=agent_with_sql,
    tools=tools,
    verbose=True,
    max_iterations=3,
    handle_parsing_errors=True,
    memory=memory,
)
# Invoke the agent with a SQL question
response_with_sql = agent_executor_sql.invoke(
    {
        "input": """what is the price on January 1st 2023 for stock_ticker ABC in my stock_price table?"""
    }
)

response_with_sql_2 = agent_executor_sql.invoke(
    {"input": """what is the average price for that stock_ticker ?"""}
)
