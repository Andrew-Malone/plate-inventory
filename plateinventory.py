import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

BACKGROUND_COLOR = "#91278F"
FONT = ("Helvetica Neue", 18)

class PlateInventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plate Inventory")
        self.setStyleSheet("background-color: " + BACKGROUND_COLOR)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create entry widgets
        self.create_entry(layout, "Monday", focus=True)
        self.create_entry(layout, "Press Remakes")
        self.create_entry(layout, "PP Scrap")
        self.create_entry(layout, "Total Good")
        self.create_label(layout, "Total Used")
        self.create_entry(layout, "Inventory Addition")
        self.create_label(layout, "Friday Total")

        # Create Export button
        export_button = QPushButton("Export")
        export_button.setStyleSheet("background-color: white; color: black; font: {}pt;".format(FONT[1]))
        layout.addWidget(export_button)

        self.setLayout(layout)

    def create_entry(self, layout, label_text, focus=False):
        entry_layout = QHBoxLayout()

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Align text to the right
        label.setStyleSheet("color: white; font: {}pt;".format(FONT[1]))
        label.setFixedWidth(150)  # Adjust width for alignment
        entry_layout.addWidget(label)

        entry = QLineEdit()
        entry.setStyleSheet("background-color: white; color: black; font: {}pt;".format(FONT[1]))
        entry.setFixedWidth(100)
        entry_layout.addWidget(entry)

        layout.addLayout(entry_layout)

        if focus:
            entry.setFocus()

    def create_label(self, layout, label_text):
        label_layout = QHBoxLayout()

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Align text to the right
        label.setStyleSheet("color: white; font: {}pt;".format(FONT[1]))
        label.setFixedWidth(150)  # Adjust width for alignment
        label_layout.addWidget(label)

        label_value = QLabel("0")
        label_value.setAlignment(Qt.AlignCenter)  # Align text to the center
        label_value.setStyleSheet("background-color: white; color: black; font: {}pt;".format(FONT[1]))
        label_value.setFixedWidth(100)
        label_layout.addWidget(label_value)

        layout.addLayout(label_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    plate_inventory_app = PlateInventoryApp()
    plate_inventory_app.show()
    sys.exit(app.exec_())
