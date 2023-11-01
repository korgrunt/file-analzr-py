from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from components.header import Header
from components.body import Body
from components.footer import Footer

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

        ################################################################################################################
        # Window and central widget
        self.setWindowTitle("Positionnement en Pourcentage")
        self.setGeometry(int(SCREEN_WIDTH*0.25/2), int(SCREEN_HEIGHT*0.25/2), int(SCREEN_WIDTH*0.75), int(SCREEN_HEIGHT*0.75))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        ################################################################################################################
        # Global layout
        global_layout = QVBoxLayout()
        central_widget.setLayout(global_layout)

        ################################################################################################################
        # Header
        header = Header()
        global_layout.addLayout(header.get_header_layout())

        ################################################################################################################
        # Body
        body = Body()
        global_layout.addLayout(body.get_body_layout())

        #################################################################################################################
        # Footer
        footer = Footer(SCREEN_WIDTH)
        global_layout.addLayout(footer.get_footer_layout())

        #######################################
        # Fix size for layout
        global_layout.setStretchFactor(header.get_header_layout(), 1)
        global_layout.setStretchFactor(body.get_body_layout(), 8)
        global_layout.setStretchFactor(footer.get_footer_layout(), 1)




window = BuildWindow()
window.show()
app.exec()