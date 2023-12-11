import mysql.connector
def get_connection():
    '''
    Return a connection to the database.
    '''
    return mysql.connector.connect(host="localhost", user="", passwd="")

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table.
    '''
    # Establish a database connection
    conn = get_connection()
    try:
        # Create a cursor object using the connection
        cursor = conn.cursor()
        # SQL query to delete a user
        query = "DELETE FROM users WHERE username = %s"
        # Execute the query
        cursor.execute(query, (username,))
        # Commit the changes
        conn.commit()
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()