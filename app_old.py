
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

def load_file_into_variable(file_path):
    file = QFile(file_path)

    if file.open(QIODevice.ReadOnly | QIODevice.Text):
        data = file.readAll()
        file.close()
        return bytes(data).decode("utf-8")  # Convert QByteArray to a string
    else:
        return None


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(1000,1000))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        btn = QPushButton('Bouton 1')
        layout.addWidget(btn, 0, 0)

        layout.addWidget(QPushButton('Button2'), 1, 0)
        layout.addWidget(QLabel('label'), 2, 0)
        layout.addWidget(QTextEdit(),3, 0)
        layout.addWidget(QCalendarWidget(), 4, 0)

        lcd_number = QLCDNumber()
        lcd_number.setMinimumHeight(50)
        lcd_number.display(5123)
        layout.addWidget(lcd_number, 5, 0)

        form_layout = QFormLayout()
        layout.addLayout(form_layout, 0, 1, 5, 1)

        line_edit = QLineEdit()
        line_edit.setText('Richnou')
        form_layout.addRow('Line Edit:', line_edit)

        form_layout.addRow('Text Edit:', QTextEdit())
        form_layout.addRow('Text Edit:', QTextEdit())

        form_layout.addRow('Time:', QTimeEdit())
        form_layout.addRow('Date:', QDateEdit())
        form_layout.addRow('Date Time:', QDateTimeEdit())

        form_layout.addRow('', QCheckBox('Signup ?'))
        colors = ['Rouge', 'Vert', 'Jaune', 'Bleu']
        color_group = QButtonGroup(self)
        color_layout = QHBoxLayout()
        for index, color in enumerate(colors):
            r = QRadioButton(color)
            color_group.addButton(r)
            color_layout.addWidget(r)
            if index == 0:
                r.setChecked(True)
        form_layout.addRow('Couleurs:', color_layout)

        combo = QComboBox()
        combo.addItem("Chouette")
        combo.addItem("Croissant")
        combo.addItem("Chocolatine")
        combo.addItems(colors)
        combo.setCurrentIndex(0)
        form_layout.addRow('Liste', combo)

        load_button = QPushButton("Charger un fichier", self)
        load_button.clicked.connect(self.load_file)
        layout.addWidget(load_button)

    def load_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Sélectionner un fichier", "",
                                                   "Fichiers texte (*.txt);;Tous les fichiers (*)")

        if file_path:
            file_data = self.load_file_into_variable(file_path)

            if file_data is not None:
                self.text_edit.setPlainText(file_data)
            else:
                self.text_edit.setPlainText("Échec de chargement du fichier.")

    def load_file_into_variable(self, file_path):
        file = QFile(file_path)

        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            data = file.readAll()
            file.close()
            return bytes(data).decode("utf-8")
        else:
            return None

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("My window title")
window.show()

app.exec()
