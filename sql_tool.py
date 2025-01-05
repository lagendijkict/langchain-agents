import sqlite3
from langchain.tools import Tool


def query_database(query: str) -> str:
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("./database/stock_data.sqlite")
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Format the result for readability
        if result:
            return "\n".join(str(row) for row in result)
        else:
            return "No results found."
    except Exception as e:
        return f"An error occurred: {e}"


# Create a LangChain Tool
sqlite_tool = Tool(
    name="SQLiteQueryTool",
    func=query_database,
    description="""Use this tool to execute SQL queries on the SQLite database. The database contains a table named 'stock_prices' with columns 'obs_id', 'stock_ticker', 'price', and 'date'. Input must be a valid SQL query.""",
)
