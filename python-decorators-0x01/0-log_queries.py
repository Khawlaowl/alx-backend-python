import sqlite3
import functools

def log_queries(func):
    """
    Decorator that logs SQL queries before executing them.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the query from the arguments (assuming it's the first argument)
        query = kwargs.get("query") if "query" in kwargs else args[0]
        print(f"Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
