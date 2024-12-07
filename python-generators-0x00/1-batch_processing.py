from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows in batches from the user_data table.

    Args:
        batch_size (int): The number of rows to fetch per batch.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    offset = 0
    while True:
        # Fetch the next batch of users
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()

        if not rows:
            break  # Stop iteration if there are no more rows

        offset += batch_size
        yield rows  # Yield the current batch of rows

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes users in batches and filters users over the age of 25.
    
    Args:
        batch_size (int): The number of rows to process in each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        # Filter users over the age of 25
        filtered_users = [user for user in batch if user['age'] > 25]
        for user in filtered_users:
            print(user)  # Process each filtered user (e.g., print their data)
