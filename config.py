from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import Tool
from langchain.prompts import PromptTemplate

load_dotenv()
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
# Tool 1: math
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0,
    model_name="gpt-3.5-turbo-16k",
)

hub_prompt = hub.pull("hwchase17/react")

# Tool 2: general
llmchain_prompt = PromptTemplate(input_variables=["query"], template="{query}")

llm_chain = llmchain_prompt | llm
# initialize the LLM tool
llm_chain_tool = Tool(
    name="Language Model",
    func=llm_chain.invoke,
    description="use this tool for general purpose queries and logic",
)

sql_prompt = PromptTemplate(
    input_variables=[
        "input",
        "tools",
        "tool_names",
        "agent_scratchpad",
        "chat_history",
    ],
    template="""
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Previous conversation history:
    {chat_history}

    Begin!

    Question: {input}
    Thought:{agent_scratchpad}
    """,
)
