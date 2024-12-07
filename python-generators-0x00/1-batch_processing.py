import seed

def stream_users_in_batches(batch_size):
    """
    Generator that fetches users from the database in batches of the specified size.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    offset = 0
    while True:
        # Fetch a batch of users
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        
        # If no rows are left, stop iteration
        if not rows:
            break
        
        yield rows  # Yield the batch of users
        offset += batch_size  # Increment the offset for the next batch

    connection.close()
    return  # Required to indicate the end of the generator


def batch_processing(batch_size):
    """
    Processes each batch by filtering users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:  # Filter users over the age of 25
                print(user)
    return "Processing complete"  # Return statement for function completion
