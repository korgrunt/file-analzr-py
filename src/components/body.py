from PySide6.QtCore import Slot
from PySide6.QtGui import QTextBlockFormat, QTextCursor
from PySide6.QtWidgets import QHBoxLayout, QWidget, QPlainTextEdit, QSizePolicy

import sys


sys.path.append("..")
from components.hex_editor import HexPlainTextEdit
from utils.encodeUtils import EncodeUtils


class Body():
    def __init__(self, parent):
        self.parent = parent
        self.body_layout = QHBoxLayout()

        body_widget = QWidget()
        # body_widget.setStyleSheet("background-color: red;")
        self.body_layout.addWidget(body_widget)

        # text areas
        # create layout horizontal for TextEditors
        horizontal_layout = QHBoxLayout()
        body_widget.setLayout(horizontal_layout)

        # Create one text editor
        self.left_edit = QPlainTextEdit()
        self.left_edit_editing = False
        self.left_edit.setPlaceholderText("Raw content")
        self.left_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Create second text editor
        self.right_edit = HexPlainTextEdit()
        self.right_edit_editing = False
        self.right_edit.setPlaceholderText("Bytes content")
        self.right_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Connexions des signaux et des slots
        self.left_edit.textChanged.connect(self.handle_text_changed_left)
        self.right_edit.textChanged.connect(self.handle_text_changed_right)

        # setup hexa editor style
        font = self.right_edit.document().defaultFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.right_edit.document().setDefaultFont(font)
        # Define marge width
        margin_format = QTextBlockFormat()
        margin_format.setLeftMargin(200)  # ajust width
        # set cursor
        cursor = QTextCursor(self.right_edit.document())
        cursor.select(QTextCursor.SelectionType.BlockUnderCursor)
        cursor.setBlockFormat(margin_format)
        self.right_edit.setTextCursor(cursor)

        # Add editor to layout
        horizontal_layout.addWidget(self.left_edit, 7)  # 7/8 de largeur
        horizontal_layout.addWidget(self.right_edit, 7)  # 7/8 de largeur

    @Slot()
    def handle_text_changed_left(self):
        if not self.right_edit_editing:
            # Répercute la modification dans plainTextEditB
            self.left_edit_editing = True
            self.parent.dataFromFileOrURI = EncodeUtils.latin_to_hex(self.left_edit.toPlainText())
            self.parent.dataFromFileOrURIRaw = self.left_edit.toPlainText()
            self.right_edit.setPlainText(self.parent.dataFromFileOrURI)
            self.left_edit_editing = False

    def update(self):
        print("body Notified")
        self.right_edit.setPlainText(self.parent.dataFromFileOrURI)

    @Slot()
    def handle_text_changed_right(self):
        if not self.left_edit_editing and len(self.right_edit.toPlainText()) % 2 == 0:
            # Répercute la modification dans plainTextEditA
            self.right_edit_editing = True
            self.parent.dataFromFileOrURI = self.right_edit.toPlainText()
            self.parent.dataFromFileOrURIRaw = self.left_edit.toPlainText()
            self.left_edit.setPlainText(EncodeUtils.hex_to_latin(self.parent.dataFromFileOrURI))
            self.right_edit_editing = False

    def get_body_layout(self):
        return self.body_layout

