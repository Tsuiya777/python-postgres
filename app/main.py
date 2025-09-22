import os
import psycopg

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "postgres_db"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "mydb"),
        user=os.getenv("DB_USER", "myuser"),
        password=os.getenv("DB_PASS", "mypassword"),
    )

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INT NOT NULL
                )
            """)

def insert_user(name, age):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))

def fetch_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, age FROM users")
            return cur.fetchall()

if __name__ == "__main__":
    print("Initializing DB...")
    init_db()
    print("Inserting sample users...")
    insert_user("Alice", 25)
    insert_user("Bob", 30)
    print("Fetching users...")
    for row in fetch_users():
        print(row)