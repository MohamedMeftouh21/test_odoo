import psycopg2
from psycopg2 import Error

def connect_to_database():
    # Connection parameters
    connection_params = {
        'host': 'localhost',
        'port': '5432',
        'dbname': 'admin',
        'user': 'odoo',
        'password': 'odoo'
    }

    try:
        # Establish connection to the admin database
        conn = psycopg2.connect(**connection_params)
        print("Successfully connected to 'admin' database!")
        return conn
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def list_database_tables(conn):
    try:
        # Create a cursor object
        cursor = conn.cursor()
        
        # Query to list all tables
        cursor.execute("""
            SELECT table_schema, table_name 
            FROM information_schema.tables 
            WHERE table_type = 'BASE TABLE'
            AND table_schema NOT IN ('pg_catalog', 'information_schema')
            ORDER BY table_schema, table_name;
        """)
        
        # Fetch and display results
        tables = cursor.fetchall()
        if tables:
            print("\nTables in 'admin' database:")
            for schema, table in tables:
                print(f"Schema: {schema}, Table: {table}")
        else:
            print("No user tables found in the database.")
            
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

def main():
    # Connect to database
    conn = connect_to_database()
    if conn:
        try:
            # List tables
            list_database_tables(conn)
        finally:
            # Always close the connection
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()