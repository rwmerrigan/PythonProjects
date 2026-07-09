import sqlite3
from icecream import ic as print

# Step 1 - Setup / Initialize Database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise


# Step 2 - Create a Table in the Database
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """
    try:
        with connection:
            connection.execute(query)
        print("Table was created!")
    except Exception as e:
        print(e)


# Step 3 - Add User to Database
def insert_user(connection, name:str, age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"User: {name} was added to your database!")
    except Exception as e:
        print(e)


# Step 4 - Query all Users in Database
def fetch_users(connection, condition: str = None) -> list[tuple]:
    query = "SELECT * FROM users"
    if condition:
        query += f" WHERE {condition}"
    
    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)


# Step 5 - Delete a User from the Database
def delete_user(connection, user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    try: 
        with connection:
            connection.execute(query,(user_id,))
        print(f"USER ID: {user_id} was deleted!")
    except Exception as e:
        print(e)


# Step 6 - Update an existing user
def update_user(connection, user_id:int, email:str):
    query = "UPDATE users SET email = ? WHERE id = ?"
    try:
        with connection:
            connection.execute(query,(email, user_id))
        print(f"User ID {user_id} has new email of {email}")
    except Exception as e:
        print(e)


# Step 7 - Add multiple users at the same time
def insert_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
    try:
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} users were added to the database")
    except Exception as e:
        print(e)
    


# Main Function Wrapper
def main():
    connection = get_connection("subscribe.db")

    x = int(input("1 - activate, 2 - freeze: "))
    while x != 2:

        try:
            # Create my table
            create_table(connection)
            start = input("Enter Option (Add, Delete, Update, Search, Add Many):").lower()
            if start == 'add':
                name  = input("Enter name: ")
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                insert_user(connection, name, age, email)
            elif start == 'search':
                print("All Users:")
                for user in fetch_users(connection):
                    print(user)
            elif start == 'delete':
                user_id = int(input("Enter User ID: "))
                delete_user(connection, user_id)
            elif start == 'update':
                user_id = int(input("Enter User ID: "))
                new_email = input("Enter a new email:")
                update_user(connection, user_id, new_email)
            elif start == 'add many':
                users = [
                    ("Chandler", 29, "friends@none.com"),
                    ("Truman", 37, "truman@theshow.com"),
                    ("Olga", 68, "siberian_grandma@gmail.com")
                    ]
                insert_users(connection, users)
            x = int(input("1 - activate, 2 - freeze: "))
        finally: 
            connection.close()

# if this file is being run directly, it calls main()
if __name__ =="__main__":
    main()



