import mysql.connector

def stream_users():
    # Establish the database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = connection.cursor(dictionary=True)

    # Execute the SQL query
    cursor.execute("SELECT * FROM user_data")

    # Yield rows one by one
    for row in cursor:
        yield row

    # Close the connection
    cursor.close()
    connection.close()
