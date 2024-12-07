import mysql.connector

def stream_user_ages():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row[0]

    cursor.close()
    connection.close()

def calculate_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    average_age = total_age / count if count else 0
    print(f"Average age of users: {average_age}")
