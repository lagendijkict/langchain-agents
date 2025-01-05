from config import llm

from langchain.agents import Tool
from langchain.chains import LLMMathChain

llm_math_custom = LLMMathChain(llm=llm)

math_tool_custom = [
    Tool(
        name="Calculator",
        func=llm_math_custom.run,
        description="useful for when you need to answer questions about math",
    )
]
