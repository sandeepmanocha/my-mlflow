import psycopg2
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


def list_tables(conn):
    """
    Lists the tables in the database.
    """
    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        if tables:
            print("Tables in the database:")
            print(tables)
            # for table in tables:
            #     print(f"- {table[0]}")
        else:
            print("No tables found in the database.")

def test_postgres_connection():
    """
    Tests the connection to a PostgreSQL database and lists the tables.
    """
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST", "localhost"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
            user=os.environ.get("POSTGRES_USER", "your_user"),
            password=os.environ.get("POSTGRES_PASSWORD", "your_password"),
            dbname=os.environ.get("POSTGRES_DB", "your_database"),
        )

        print("Connection to PostgreSQL successful!")
        list_tables(conn)
        conn.close()
    except psycopg2.OperationalError as e:
        print(f"Could not connect to PostgreSQL: {e}")

if __name__ == "__main__":
    test_postgres_connection()
