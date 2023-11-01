from PySide6.QtWidgets import QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QWidget


class Footer():
    def __init__(self, SCREEN_WIDTH):
        self.footer_layout = QHBoxLayout()
        footer_widget = QWidget()
        # footer_widget.setStyleSheet("background-color: yellow;")
        self.footer_layout.addWidget(footer_widget)

        # Utilisez un QHBoxLayout pour organiser les boutons de manière horizontale dans le footer
        button_layout = QHBoxLayout()
        footer_widget.setLayout(button_layout)

        # Ajoutez un bouton à 20% de la largeur
        button1 = QPushButton("Save as")
        button_layout.addWidget(button1)
        button_layout.setStretchFactor(button1, 1)

        # Ajoutez un bouton à 30% de la largeur
        button2 = QPushButton("Open file")
        button_layout.addWidget(button2)
        button_layout.setStretchFactor(button2, 1)

        # Créez un espace extensible pour pousser le bouton suivant vers la droite
        spacer = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        spacer.changeSize(int(SCREEN_WIDTH * 0.6), 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        button_layout.addItem(spacer)

        # Ajoutez un bouton à 30% de la largeur
        button3 = QPushButton("Open metadata")
        button_layout.addWidget(button3)
        button_layout.setStretchFactor(button3, 1)


    def get_footer_layout(self):
        return self.footer_layout
