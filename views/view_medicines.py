from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLabel
)

from models.db_manager import get_connection


class ViewMedicines(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("All Medicines")
        self.setGeometry(200, 200, 900, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.total_label = QLabel("Total Pending: ₹ 0")
        self.layout.addWidget(self.total_label)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM medicine ORDER BY net_rate ASC")
        records = cursor.fetchall()

        self.table.setRowCount(len(records))
        self.table.setColumnCount(8)

        self.table.setHorizontalHeaderLabels([
            "ID", "Medicine Name", "Company",
            "Net Rate", "MRP", "Stockiest",
            "Paid Status", "Paid Amount"
        ])

        total_pending = 0

        for row_index, row_data in enumerate(records):
            for col_index, col_data in enumerate(row_data):
                self.table.setItem(
                    row_index,
                    col_index,
                    QTableWidgetItem(str(col_data))
                )

            # --- Pending Calculation ---
            net_rate = float(row_data[3])
            paid_status = row_data[6]
            paid_amount = float(row_data[7])

            if paid_status == "Unpaid":
                total_pending += net_rate
            elif paid_status == "Half Paid":
                total_pending += (net_rate - paid_amount)

        self.total_label.setText(f"Total Pending: ₹ {total_pending}")

        conn.close()
