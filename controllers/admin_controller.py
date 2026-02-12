from models.db_manager import get_connection


def add_medicine(medicine_name, company_name, net_rate, mrp,
                 stockiest, paid_status, paid_amount):

    if paid_status == "Paid":
        remaining_amount = 0
    elif paid_status == "Unpaid":
        remaining_amount = net_rate
        paid_amount = 0
    else:  # Half Paid
        remaining_amount = net_rate - paid_amount

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO medicines (
            medicine_name,
            company_name,
            net_rate,
            mrp,
            stockiest,
            paid_status,
            paid_amount,
            remaining_amount
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        medicine_name,
        company_name,
        net_rate,
        mrp,
        stockiest,
        paid_status,
        paid_amount,
        remaining_amount
    ))

    conn.commit()
    conn.close()
