import seed

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database with the given page size and offset.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    # SQL query to fetch users with pagination (LIMIT and OFFSET)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    
    rows = cursor.fetchall()
    connection.close()
    return rows  # Return the fetched rows

def lazy_paginate(page_size):
    """
    Generator that lazily loads pages of user data.
    """
    offset = 0
    while True:
        # Get the next page of users
        page = paginate_users(page_size, offset)
        
        if not page:  # If no more data is available, stop the iteration
            break
        
        yield page  # Yield the page of users
        offset += page_size  # Increment offset for the next page
