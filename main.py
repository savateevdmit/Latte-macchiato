from PyQt5 import QtWidgets, QtCore, uic
from sys import exit, argv
import sqlite3

from PyQt5.QtWidgets import QMainWindow


class addEditForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/addEditCoffeeForm.ui', self)


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зёрнах',
                                                    'Описание вкуса', 'Цена', 'Объём упаковки'])
        self.addOrEdit.clicked.connect(self.edit_coffee)
        self.con = sqlite3.connect("data/coffee.db")
        self.cur = self.con.cursor()
        self.tbl()

    def edit_coffee(self):
        self.addEditForm = addEditForm()
        self.addEditForm.add.clicked.connect(self.add)
        self.addEditForm.show()

    def tbl(self):
        data = self.cur.execute(f"""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            for g in range(7):
                self.tableWidget.setItem(
                    i, g, QtWidgets.QTableWidgetItem(str(data[i][g]))
                )

    def add(self):
        data = self.cur.execute(f"""SELECT * FROM coffee""").fetchall()
        id = len(data) + 1
        varietyName = self.addEditForm.varietyName.text()
        roasting = self.addEditForm.degreeOfRoast.text()
        type = self.addEditForm.groundOrBeans.text()
        description = self.addEditForm.description.text()
        price = self.addEditForm.price.text()
        volume = self.addEditForm.volume.text()
        self.cur.execute(
            "INSERT INTO [coffee] VALUES (?, ?, ?, ?, ?, ?, ?)",
            (id, varietyName, roasting, type, description, price, volume),
        )
        self.con.commit()
        self.tbl()
        self.addEditForm.hide()

    def edit(self):
        id = self.addEditForm.id.text()
        varietyName = self.addEditForm.varietyName.text()
        roasting = self.addEditForm.degreeOfRoast.text()
        type = self.addEditForm.groundOrBeans.text()
        description = self.addEditForm.description.text()
        price = self.addEditForm.price.text()
        volume = self.addEditForm.volume.text()
        self.cur.execute(
            """UPDATE [coffee] SET [Название_сорта]=?, [Степень_обжарки]=?, [Молотый_В_зёрнах]=?, Описание_вкуса=?, Цена=?, Объём_упаковки=? WHERE ID=?""",
            (varietyName, roasting, type, description, price, volume, id),
        )
        self.con.commit()
        self.tbl()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    ex = MainForm()
    ex.show()
    exit(app.exec())
