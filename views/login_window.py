from views.admin_window import AdminWindow

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from controllers.login_controller import authenticate_user


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medicine Price Optimizer - Login")
        self.setFixedSize(350, 250)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Admin Login")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        layout.addWidget(self.username_input)

        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Login Button
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        role = authenticate_user(username, password)

        if role:
            QMessageBox.information(self, "Success", "Login Successful!")

            if role == "admin":
                self.admin_window = AdminWindow()
                self.admin_window.show()

            self.close()
            
        else:
            QMessageBox.warning(self, "Error", "Invalid Username or Password")
