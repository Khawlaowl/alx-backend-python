import sqlite3
import functools
from datetime import datetime  # Importing datetime to log the timestamp

def log_queries(func):
    """
    Decorator that logs SQL queries before executing them with a timestamp.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the query from the arguments (assuming it's the first argument)
        query = kwargs.get("query") if "query" in kwargs else args[0]
        
        # Log the timestamp and query
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Executing SQL query: {query}")
        
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
