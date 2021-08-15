# Author: Taylor Czerwinski
# Summer 2021

from db_manager import DBManager
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

# Search for flights by date dialog
class Date_Dialog(QDialog):
    # Constructor for Date_Dialog object
    def __init__(self, parent=None):  # parent is sent during instantiation
        super(Date_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    # Sets up Date_Dialog's attributes
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 535)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(230, 0, 312, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.show_flights)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 210, 721, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 120)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Flight Number", "Origin", "Destination", "Departure Time", "Arrival Time", "Status"])

        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(20, 10, 113, 32))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.close)
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(630, 490, 113, 32))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.close)

        self.gif = QtWidgets.QLabel(Dialog)
        self.gif.setGeometry(QtCore.QRect(30, 50, 171, 121))
        self.gif.setObjectName("gif")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 180, 101, 21))
        movie = QtGui.QMovie('Images/airplane6.gif')
        self.gif.setScaledContents(True)
        self.gif.setMovie(movie)
        movie.start()
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.date = QtWidgets.QLineEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(130, 180, 113, 21))
        self.date.setObjectName("date")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Translates Date_Dialog's attributes to user interface
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search Date"))
        self.back.setText(_translate("Dialog", "Back"))
        self.exit.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Flights On:"))

    # Displays flight information of the flights occurring on qDate
    def show_flights(self, qDate):
        db_manager = DBManager()
        flight_numbers = db_manager.get_flight_numbers(qDate)
        self.date.setText(qDate.toString("MMM d,  yyyy"))
        num_rows = len(flight_numbers)
        self.tableWidget.setRowCount(num_rows)
        table_row = 0
        for row in flight_numbers:
            flight_info = db_manager.get_flight_info(row[0])
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(flight_info[0])))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(str(flight_info[1])))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(str(flight_info[2])))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(flight_info[3].strftime('%I:%M %p')))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(flight_info[4].strftime('%I:%M %p')))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(flight_info[5])))
            table_row += 1

