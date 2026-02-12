from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout,
    QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from controllers.search_controller import search_medicine


class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Medicine")
        self.setFixedSize(700, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Search Cheapest Medicine")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter Medicine Name")
        layout.addWidget(self.search_input)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.handle_search)
        layout.addWidget(search_button)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Medicine", "Company", "Net Rate",
            "MRP", "Stockiest",
            "Paid Status", "Paid Amount",
            "Remaining"
        ])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def handle_search(self):
        medicine_name = self.search_input.text()
        result = search_medicine(medicine_name)

        self.table.setRowCount(0)

        if result:
            self.table.setRowCount(1)

            for col, value in enumerate(result):
                self.table.setItem(0, col, QTableWidgetItem(str(value)))
