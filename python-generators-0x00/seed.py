import mysql.connector

def connect_to_prodev():
    """
    Establish a connection to the ProDev database.
    """
    return mysql.connector.connect(
        host="localhost",
        user="your_username",    # Replace with your DB username
        password="your_password",  # Replace with your DB password
        database="your_database"   # Replace with your database name
    )


def seed_database():
    """
    Populate the `user_data` table with sample data.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()

    # Create the user_data table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        age INT
    )
    """)

    # Sample data to insert into the table
    sample_users = [
        ("00234e50-34eb-4ce2-94ec-26e3fa749796", "Dan Altenwerth Jr.", "Molly59@gmail.com", 67),
        ("006bfede-724d-4cdd-a2a6-59700f40d0da", "Glenda Wisozk", "Miriam21@gmail.com", 119),
        ("006e1f7f-90c2-45ad-8c1d-1275d594cc88", "Daniel Fahey IV", "Delia.Lesch11@hotmail.com", 49),
        ("00af05c9-0a86-419e-8c2d-5fb7e899ae1c", "Ronnie Bechtelar", "Sandra19@yahoo.com", 22),
        ("00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4", "Alma Bechtelar", "Shelly_Balistreri22@hotmail.com", 102),
        ("01187f09-72be-4924-8a2d-150645dcadad", "Jonathon Jones", "Jody.Quigley-Ziemann33@yahoo.com", 116),
        ("01ab6c5d-7ae2-4968-991a-d63e93d8d025", "Forrest He
