from PySide6.QtWidgets import QHBoxLayout, QWidget, QPlainTextEdit, QSizePolicy


class Body():
    def __init__(self):
        self.body_layout = QHBoxLayout()

        body_widget = QWidget()
        # body_widget.setStyleSheet("background-color: red;")
        self.body_layout.addWidget(body_widget)

        # text areas
        # create layout horizontal for TextEditors
        horizontal_layout = QHBoxLayout()
        body_widget.setLayout(horizontal_layout)

        # Create one text editor
        left_edit = QPlainTextEdit()
        left_edit.setPlaceholderText("Raw content")
        # size
        left_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Create osecondne text editor
        right_edit = QPlainTextEdit()
        right_edit.setPlaceholderText("Bytes content")
        # size
        right_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Add editor to layout
        horizontal_layout.addWidget(left_edit, 7)  # 7/8 de largeur
        horizontal_layout.addWidget(right_edit, 7)  # 7/8 de largeur

    def get_body_layout(self):
        return self.body_layout

