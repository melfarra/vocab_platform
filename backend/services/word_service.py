from backend.config import get_database_connection

def save_word_to_history(word, details):
    """
    Save a word and its details to the database.
    """
    conn = get_database_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO word_history (word, details) VALUES (%s, %s)",
            (word, details)
        )
        conn.commit()

def get_word_history():
    """
    Retrieve the history of all generated words.
    """
    conn = get_database_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT word, details, created_at FROM word_history ORDER BY created_at DESC")
        return cur.fetchall()
