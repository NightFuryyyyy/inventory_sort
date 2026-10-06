from pathlib import Path
from dataclasses import dataclass, fields
from datetime import date
import json
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from form import Ui_Form


if getattr(sys, "frozen", False):
    APP_DIR = Path(sys.executable).resolve().parent
else:
    APP_DIR = Path(__file__).resolve().parent

@dataclass
class Item:
    id: int
    name: str
    category: str
    quantity: int
    price: float
    restock_date: date

class Form(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sort_field_comboBox.currentIndexChanged.connect(self.sort_inventory)
        self.sort_order_comboBox.currentIndexChanged.connect(lambda: self.sort_inventory(self.sort_field_comboBox.currentIndex()))
        self.open_button.clicked.connect(self.open_file)

    def sort_inventory(self, index):
        self.inventory = merge_sort(self.inventory, fields(Item)[index].name, self.sort_order_comboBox.currentIndex() == 1)
        self.populate_table()

    def populate_table(self):
        self.tableWidget.setRowCount(len(self.inventory))
        self.tableWidget.setColumnCount(len(fields(Item)))
        self.tableWidget.setHorizontalHeaderLabels([self.sort_field_comboBox.itemText(i) for i in range(self.sort_field_comboBox.count())])

        for row, item in enumerate(self.inventory):
            for col, field in enumerate(fields(Item)):
                value = getattr(item, field.name)
                tableWidgetItem = QTableWidgetItem(str(value))
                if (isinstance(value, (int, float))):
                    tableWidgetItem.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.tableWidget.setItem(row, col, tableWidgetItem)
    
    def open_file(self):
        try:
            file_path_str, _ = QFileDialog.getOpenFileName(
                self, 
                "Open File", 
                str(APP_DIR), 
                "JSON Files (*.json)"
            )

            if file_path_str:
                file_path = Path(file_path_str)
            else:
                return

            with open(file_path) as f:
                dict_list = json.load(f)

            self.inventory = [Item(
                id=item["id"],
                name=item["name"],
                category=item["category"],
                quantity=item["quantity"],
                price=item["price"],
                restock_date=date.fromisoformat(item["restock_date"]),
            ) for item in dict_list]

            self.populate_table()
            self.file_label.setText(file_path.name)
            self.sort_field_comboBox.setCurrentIndex(0)
            self.sort_order_comboBox.setCurrentIndex(0)

        except:
            QMessageBox.critical(self, "Error", "Invalid JSON schema", QMessageBox.StandardButton.Ok)

def merge_sort(arr: list, attr: str, desc: bool = False) -> list:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], attr, desc=desc)
    right = merge_sort(arr[mid:], attr, desc=desc)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        a, b = getattr(left[i], attr), getattr(right[j], attr)
        take_left = (a >= b) if desc else (a <= b)
        if take_left:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()
    app.exec()