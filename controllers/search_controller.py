from models.db_manager import get_connection


def search_medicine(medicine_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT medicine_name, company_name, net_rate,
               mrp, stockiest, paid_status,
               paid_amount, remaining_amount
        FROM medicines
        WHERE medicine_name LIKE ?
        ORDER BY net_rate ASC
        LIMIT 1
    """, ('%' + medicine_name + '%',))

    result = cursor.fetchone()
    conn.close()

    return result
