
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton

class PopupWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pop up")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        text_edit = QTextEdit()
        layout.addWidget(text_edit)

        up_button = QPushButton("Up", self)
        up_button.clicked.connect(self.up_button_clicked)
        layout.addWidget(up_button)

        self.setLayout(layout)

    def up_button_clicked(self):
        print("btn clicked")