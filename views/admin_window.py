from views.search_window import SearchWindow
from views.view_medicines import ViewMedicines

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QComboBox,
    QMessageBox, QFormLayout
)
from PyQt5.QtCore import Qt
from controllers.admin_controller import add_medicine


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Dashboard")
        self.setFixedSize(400, 500)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Add Medicine")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        form_layout = QFormLayout()

        self.medicine_name = QLineEdit()
        self.company_name = QLineEdit()
        self.net_rate = QLineEdit()
        self.mrp = QLineEdit()
        self.stockiest = QLineEdit()

        self.paid_status = QComboBox()
        self.paid_status.addItems(["Paid", "Unpaid", "Half Paid"])
        self.paid_status.currentIndexChanged.connect(self.toggle_paid_amount)


        self.paid_amount = QLineEdit()

        form_layout.addRow("Medicine Name:", self.medicine_name)
        form_layout.addRow("Company Name:", self.company_name)
        form_layout.addRow("Net Rate:", self.net_rate)
        form_layout.addRow("MRP:", self.mrp)
        form_layout.addRow("Stockiest:", self.stockiest)
        form_layout.addRow("Paid Status:", self.paid_status)
        form_layout.addRow("Paid Amount:", self.paid_amount)

        layout.addLayout(form_layout)

        save_button = QPushButton("Save Medicine")
        save_button.clicked.connect(self.save_medicine)
        layout.addWidget(save_button)

        # Search Medicine Button
        search_button = QPushButton("Search Medicine")
        search_button.clicked.connect(self.open_search)
        layout.addWidget(search_button)

        view_button = QPushButton("View All Medicines")
        view_button.clicked.connect(self.open_view)
        layout.addWidget(view_button)



        self.setLayout(layout)


    def open_view(self):
        self.view_window = ViewMedicines()
        self.view_window.show()


    def toggle_paid_amount(self):
        status = self.paid_status.currentText()

        if status == "Half Paid":
            self.paid_amount.setDisabled(False)
        else:
            self.paid_amount.setText("0")
            self.paid_amount.setDisabled(True)


    def open_search(self):
        self.search_window = SearchWindow()
        self.search_window.show()


    def clear_form(self):
        self.medicine_name.clear()
        self.company_name.clear()
        self.net_rate.clear()
        self.mrp.clear()
        self.stockiest.clear()
        self.paid_amount.clear()
        self.paid_status.setCurrentIndex(0)


    def save_medicine(self):
        try:
            medicine_name = self.medicine_name.text()
            company_name = self.company_name.text()

            if not self.medicine_name.text() or not self.company_name.text():
                QMessageBox.warning(self, "Error", "Please fill all required fields")
            return

            net_rate = float(self.net_rate.text())
            mrp = float(self.mrp.text())
            stockiest = self.stockiest.text()
            paid_status = self.paid_status.currentText()
            paid_amount = float(self.paid_amount.text())

            add_medicine(
                medicine_name,
                company_name,
                net_rate,
                mrp,
                stockiest,
                paid_status,
                paid_amount
            )

            QMessageBox.information(self, "Success", "Medicine Added Successfully!")
            self.clear_form()


        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
