from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit


class Header():
    def __init__(self):
        self.header_layout = QHBoxLayout()
        header_widget = QWidget()
        header_widget.setStyleSheet("background-color: lightblue;")
        self.header_layout.addWidget(header_widget)

        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Http, https, ftp, sftp")  # Définissez le texte du placeholder

        button = QPushButton("Fetch URI")

        # LineEdit 80% width
        self.header_layout.addWidget(line_edit)
        self.header_layout.addWidget(button)
        self.header_layout.setStretchFactor(line_edit, 7)  # Body prend 60%
        self.header_layout.setStretchFactor(button, 3)

    def get_header_layout(self):
        return self.header_layout
