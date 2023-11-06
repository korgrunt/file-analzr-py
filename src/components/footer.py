import sys

from PySide6.QtCore import QIODevice
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class Footer():

    def __init__(self, parent, SCREEN_WIDTH):
        self.footer_layout = QHBoxLayout()
        footer_widget = QWidget()
        self.footer_layout.addWidget(footer_widget)
        self.parent = parent
        footer_layout = QHBoxLayout()
        footer_widget.setLayout(footer_layout)

        button1 = QPushButton("Save as")
        button1.clicked.connect(self.save_edited_file)
        footer_layout.addWidget(button1)
        footer_layout.setStretchFactor(button1, 1)


        button2 = QPushButton("Open file", self.parent)
        button2.clicked.connect(self.parent.load_file)
        footer_layout.addWidget(button2)
        footer_layout.setStretchFactor(button2, 1)

        self.error_and_file_date_label = QLabel("")
        self.error_and_file_date_label.setStyleSheet("color: red;")
        footer_layout.addWidget(self.error_and_file_date_label)

        self.exifMetaData = QPlainTextEdit()
        self.exifMetaData.setReadOnly(True)
        self.exifMetaData.setFixedWidth(500)

        self.exifMetaData.setPlaceholderText("Exif metadata (for image only)")
        self.exifMetaData.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        footer_layout.addWidget(self.exifMetaData)

        spacer = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        spacer.changeSize(int(SCREEN_WIDTH * 0.6), 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        footer_layout.addItem(spacer)

        button3 = QPushButton("Export metadata")
        footer_layout.addWidget(button3)
        footer_layout.setStretchFactor(button3, 1)
        button3.clicked.connect(self.export_exif_data)


    def export_exif_data(self):
        self.parent.save_to_file(self.exifMetaData.toPlainText())

    def save_edited_file(self):
        self.parent.save_to_file(self.parent.dataFromFileOrURI)

    def update(self):
        print("footer Notified")
        self.error_and_file_date_label.setText(self.parent.error_message)

        self.error_and_file_date_label.setStyleSheet("color: red;")
    def get_footer_layout(self):
        return self.footer_layout
