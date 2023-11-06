import requests
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit, QLabel, QVBoxLayout, QPlainTextEdit
import time
import re
from threading import Timer
import sys

sys.path.append("..")
from utils.encodeUtils import EncodeUtils


def setTimeout(fn, ms, *args, **kwargs):
    t = Timer(ms / 1000., fn, args=args, kwargs=kwargs)
    t.start()
    return t

class Header():
    def __init__(self, parent):

        self.parent = parent
        self.header_layout = QVBoxLayout()
        self.input_header_layout = QHBoxLayout()

        self.header_request = QPlainTextEdit()
        self.header_request.setPlaceholderText("Headers HTTP de la requête")
        self.header_request.setReadOnly(True)
        self.http_request_layout = QHBoxLayout()
        self.http_request_layout.addWidget(self.header_request)




        header_widget = QWidget()
        header_widget.setStyleSheet("background-color: lightblue;")
        self.input_header_layout.addWidget(header_widget)

        self.input_url = QLineEdit()
        self.input_url.setPlaceholderText("Http, https, ftp, sftp")  # Définissez le texte du placeholder

        self.button = QPushButton("Fetch URI")

        self.button.setStyleSheet("background-color: #0000FF;")

        self.input_header_layout.addWidget(self.input_url)
        self.input_header_layout.addWidget(self.button)
        self.input_header_layout.setStretchFactor(self.input_url, 7)  # Body prend 60%
        self.input_header_layout.setStretchFactor(self.button, 3)

        self.button.clicked.connect(self.fetch_url)

        self.header_layout.addLayout(self.input_header_layout)
        self.header_layout.addLayout(self.http_request_layout)

    def get_header_layout(self):
        return self.header_layout

    def is_valid_url(self, url):
        url_pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

        if re.match(url_pattern, url):
            return True
        else:
            return False
    def display_bad_url_error(self):
        print("no fetch_url")
        self.button.setText("Url invalide")
        self.button.setStyleSheet("background-color: #ac1416;")
        setTimeout(self.reinitButtonText, 2000)


    def reinitButtonText(self):
        self.button.setStyleSheet("background-color: #0000FF;")
        self.button.setText("Fetch URI")
        self.button.setEnabled(True)

    def update(self):
        print("header Notified")

    def fetch_url(self):
        try:
            self.button.setEnabled(False)
            self.button.setText("Fetching...")
            if (not self.is_valid_url(self.input_url.text())):
                self.display_bad_url_error()
                return
            response = requests.get(self.input_url.text())

            if response.status_code == 200:
                print("response.data")
                self.parent.dataFromFileOrURI = EncodeUtils.utf8_to_hex(response.text)
                self.header_request.setPlainText(str(response.headers).replace("',", "',\n").replace("{", "").replace("}", ""))

                self.parent.progagateUpdate()
                self.reinitButtonText()

            else:
                print(f"Erreur de requête. Status Code: {response.status_code}")
        except ZeroDivisionError as e:
            # Gestion de l'exception
            print(f"Une erreur s'est produite : {e}")


