from models.db_manager import get_connection


def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]  # return role (admin/user)
    return None
