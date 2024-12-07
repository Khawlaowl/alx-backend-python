import mysql.connector

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM user_data")
    total_users = cursor.fetchone()["total"]

    for offset in range(0, total_users, batch_size):
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        yield cursor.fetchall()

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        # Process users over the age of 25
        processed_users = [user for user in batch if user["age"] > 25]
        for user in processed_users:
            print(user)
