import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSlot

BACKGROUND_COLOR = "#91278F"
FONT = ("Helvetica Neue", 18)

class PlateInventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plate Inventory")
        self.setStyleSheet("background-color: " + BACKGROUND_COLOR)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Create entry widgets
        self.entries = []
        self.create_entry("Monday Start", focus=True)
        self.create_entry("Press Remakes")
        self.create_entry("PP Scrap")
        self.create_entry("Total Good")
        self.total_used_label = self.create_label("Total Used")
        self.create_entry("Inventory Addition")
        self.friday_total_label = self.create_label("Friday Total")

        # Create Export button
        export_button = QPushButton("Export")
        export_button.setStyleSheet("""
                            QPushButton {{
                                background-color: white; 
                                color: black; 
                                font: {0}pt; 
                                border: 2px solid black;
                            }}
                            QPushButton:pressed {{
                                background-color: #B9B9B9;  /* Change to desired color */
                            }}
                            """.format(FONT[1]))
        self.layout.addWidget(export_button)

        self.setLayout(self.layout)

    def create_entry(self, label_text, focus=False):
        entry_layout = QHBoxLayout()

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Align text to the right
        label.setStyleSheet("color: white; font: {}pt;".format(FONT[1]))
        label.setFixedWidth(150)  # Adjust width for alignment
        entry_layout.addWidget(label)

        entry = QLineEdit()
        entry.setStyleSheet("background-color: white; color: black; font: {}pt;".format(FONT[1]))
        entry.setFixedWidth(70)
        entry_layout.addWidget(entry)

        self.entries.append(entry)
        entry.textChanged.connect(self.update_totals)  # Connect signal to update totals

        self.layout.addLayout(entry_layout)

        if focus:
            entry.setFocus()

    def create_label(self, label_text):
        label_layout = QHBoxLayout()

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Align text to the right
        label.setStyleSheet("color: white; font: {}pt;".format(FONT[1]))
        label.setFixedWidth(150)  # Adjust width for alignment
        label_layout.addWidget(label)

        label_value = QLabel("0")
        label_value.setAlignment(Qt.AlignCenter)  # Align text to the center
        label_value.setStyleSheet("background-color: #c7c7c7; color: black; font: {}pt;".format(FONT[1]))
        label_value.setFixedWidth(70)
        label_layout.addWidget(label_value)

        self.layout.addLayout(label_layout)

        return label_value

    @pyqtSlot()
    def update_totals(self):
        press_remakes = int(self.entries[1].text()) if self.entries[1].text().isdigit() else 0
        pp_scrap = int(self.entries[2].text()) if self.entries[2].text().isdigit() else 0
        total_good = int(self.entries[3].text()) if self.entries[3].text().isdigit() else 0

        total_used = press_remakes + pp_scrap + total_good
        self.total_used_label.setText(str(total_used))

        monday = int(self.entries[0].text()) if self.entries[0].text().isdigit() else 0
        inventory_addition = int(self.entries[-1].text()) if self.entries[-1].text().isdigit() else 0

        friday_total = monday - total_used + inventory_addition
        self.friday_total_label.setText(str(friday_total))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plate_inventory_app = PlateInventoryApp()
    plate_inventory_app.show()
    sys.exit(app.exec_())
