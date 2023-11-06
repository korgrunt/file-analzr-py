from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPlainTextEdit
import re
def is_hexadecimal(text):
    return bool(re.match(r'^[0-9A-Fa-f]*$', text))
class HexPlainTextEdit(QPlainTextEdit):
    def keyPressEvent(self, event):
        if is_hexadecimal(event.text()):
            super().keyPressEvent(event)
        elif event.key() == Qt.Key.Key_Backspace or event.key() == Qt.Key.Key_Delete:
            super().keyPressEvent(event)
        else:
            event.ignore()