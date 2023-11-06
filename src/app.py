import json
import os
import re
import time
from PySide6.QtCore import QIODevice, QFile, QByteArray
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFileDialog
from PIL import Image
from io import BytesIO
from components.header import Header
from components.body import Body
from components.footer import Footer
from utils.encodeUtils import EncodeUtils

# Get system and screen info
app = QApplication([])
screen = app.primaryScreen()
geometry = screen.geometry()

# Conctants
SCREEN_WIDTH = geometry.width()
SCREEN_HEIGHT = geometry.height()




class BuildWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # STate
        self.dataFromFileOrURI = "" # always stored as hexa
        self.dataFromFileOrURIRaw = "" # always stored as hexa
        self.url = ""
        self.metaData = ""
        self.error_message = ""

        # Component


        # Window and central widget
        self.setWindowTitle("Python File Analyzer")
        self.setGeometry(int(SCREEN_WIDTH*0.25/2), int(SCREEN_HEIGHT*0.25/2), int(SCREEN_WIDTH*0.75), int(SCREEN_HEIGHT*0.75))


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Global layout
        global_layout = QVBoxLayout()
        central_widget.setLayout(global_layout)

        # Header
        self.header = Header(self)
        global_layout.addLayout(self.header.get_header_layout())

        # Body
        self.body = Body(self)
        global_layout.addLayout(self.body.get_body_layout())

        # Footer
        self.footer = Footer(self, SCREEN_WIDTH)
        global_layout.addLayout(self.footer.get_footer_layout())

        # Fix size for layout
        global_layout.setStretchFactor(self.header.get_header_layout(), 2)
        global_layout.setStretchFactor(self.body.get_body_layout(), 7)
        global_layout.setStretchFactor(self.footer.get_footer_layout(), 1)

    def load_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Sélectionner un fichier", "",
                                                   "Fichiers texte (*.txt);;Tous les fichiers (*)")

        if file_path:
            file_data = self.load_file_into_variable(file_path)

            if file_data is not None:
                self.dataFromFileOrURI = EncodeUtils.encode_to_hex_from_file(file_data)
                self.body.right_edit.setPlainText(self.dataFromFileOrURI)
                self.body.left_edit.setPlainText(EncodeUtils.decode_to_latin_from_file(self.dataFromFileOrURI))
            else:
                self.footer.error_and_file_date_label.setText("Échec de chargement du fichier.")
                self.footer.error_and_file_date_label.setStyleSheet("color: red;")

    def is_image(self, str):
        regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
        p = re.compile(regex)
        if (str == None):
            return False
        if (re.search(p, str)):
            return True
        return False

    def progagateUpdate(self):
        self.header.update()
        self.body.update()
        self.footer.update()

    def displayImgMetadata(self, exif_date):
        if exif_date:
            exif_dict = {}
            for tag, value in exif_date.items():
                title = EncodeUtils.tagCodeToTagTitle(tag)
                exif_dict[title] = str(value)
        exif_as_json = json.dumps(exif_dict, indent=4)
        self.footer.exifMetaData.setPlainText(exif_as_json)

    def load_file_into_variable(self, file_path):
        print("file_path")
        print(file_path)
        print(self.is_image(file_path))

        file = QFile(file_path)

        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            if(self.is_image(file_path)):
                try:
                    data = QByteArray(file.readAll())
                    image = Image.open(file_path)

                    # Lire les données EXIF
                    exif_data = image._getexif()
                    self.displayImgMetadata(exif_data)
                except:
                    print("Can't explore exif data on this file")
                data = file.readAll()


            file.close()


            self.displayFileDateInformation(file_path)
            return data
        else:
            return None

    def formatSizeString(self, size):
        if size < 1024:
            return f"{size} octets"
        elif size < 1024 ** 2:  # Ko
            return f"{size / 1024:.2f} Ko"
        elif size < 1024 ** 3:  # Mo
            return f"{size / (1024 ** 2):.2f} Mo"
        else:  # Go
            return f"{size / (1024 ** 3):.2f} Go"

    def displayFileDateInformation(self, file_path):
        file_informations = os.stat(file_path)

        creation_date = time.ctime(file_informations.st_ctime)
        modification_date = time.ctime(file_informations.st_mtime)
        acces_date = time.ctime(file_informations.st_atime)
        size = self.formatSizeString(os.path.getsize(file_path))
        self.footer.error_and_file_date_label.setText(f"File open({file_path}) \nSize: {size} \nCreation date: {creation_date}  \nModification date: {modification_date}  \nAccess date: {acces_date}")
        self.footer.error_and_file_date_label.setStyleSheet("color: green;")


    def save_to_file(self, data):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Sauvegarder le fichier", "",
                                                   "Fichiers texte (*.txt);;Tous les fichiers (*)", options=options)


        print("file_path")
        print(file_path)
        encoding_for_file = EncodeUtils.get_encoding(file_path)
        fileContent = data
        if(self.is_image(file_path)):
            image = Image.open(BytesIO(data))
            image.save(file_path)
            return
        if(encoding_for_file == "bin"):
            fileContent = BytesIO(data)
        if file_path:
            try:
                with open(file_path, 'w', encoding=encoding_for_file) as file:
                    file.write(fileContent)
            except Exception as e:
                self.error_message = f"Erreur lors de la sauvegarde du fichier : {e}"
                self.progagateUpdate()




window = BuildWindow()
window.show()
app.exec()
