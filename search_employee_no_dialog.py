# Author: Taylor Czerwinski
# Summer 2021

from db_manager import DBManager
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

# Search by employee number dialog
class Employee_No_Dialog(QDialog):
    # Constructor to make an Employee_No_Dialog object
    def __init__(self, parent=None):  # parent is sent during instantiation
        super(Employee_No_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    # Sets up Employee_No_Dialog's attributes
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(760, 471)
        self.picture = QtWidgets.QLabel(Dialog)
        self.picture.setGeometry(QtCore.QRect(0, 50, 421, 401))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("Images/airplane8.png"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.close)
        self.back.setAutoDefault(False)
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(630, 430, 113, 32))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.close)
        self.exit.setAutoDefault(False)

        self.search = QtWidgets.QLineEdit(Dialog)
        self.search.setGeometry(QtCore.QRect(390, 10, 113, 21))
        self.search.setObjectName("search")
        self.search.returnPressed.connect(self.search_employee_no)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 50, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 80, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(470, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(570, 50, 113, 21))
        self.name.setObjectName("name")
        self.salary = QtWidgets.QLineEdit(Dialog)
        self.salary.setGeometry(QtCore.QRect(570, 80, 113, 21))
        self.salary.setObjectName("salary")
        self.years_flown = QtWidgets.QLineEdit(Dialog)
        self.years_flown.setGeometry(QtCore.QRect(570, 110, 113, 21))
        self.years_flown.setObjectName("years_flown")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(440, 190, 311, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 155)
        self.tableWidget.setColumnWidth(1, 155)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Flight Number", "Flight Day"])
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(440, 160, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Translates Employee_No_Dialog's attributes to user interface
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search Employee Number"))
        self.back.setText(_translate("Dialog", "Back"))
        self.exit.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Employee Number:"))
        self.label_2.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Salary:"))
        self.label_4.setText(_translate("Dialog", "Years Flown:"))
        self.label_5.setText(_translate("Dialog", "Upcoming Schedule:"))

    # Retrieves and displays an employee's record based on the employee number entered in the search attribute
    def search_employee_no(self):
        employee_no = self.search.text()
        db_manager = DBManager()
        employee = db_manager.get_employee_stat(employee_no)
        if employee is None:
            return
        hours = db_manager.invoke_proc(employee_no)
        if hours[1] is None:
            flight_hours = 0
        else:
            flight_hours = round(hours[1], 2)
        flight_info = db_manager.work_flights(hours[0])
        print(flight_info)
        self.display_records(employee, flight_hours, flight_info)

    # Displays employee information and their upcoming flights
    def display_records(self, employee, flight_hours, flight_info):
        print("FLIGHT INFO")
        print(flight_info)
        self.name.setText(employee[1])
        print(employee[2])
        self.salary.setText("{:,}".format(employee[2]))
        self.years_flown.setText(format(flight_hours, ","))
        num_rows = len(flight_info)
        self.tableWidget.setRowCount(num_rows)
        table_row = 0
        for row in flight_info:
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1].strftime("%B %d,  %Y")))
            table_row += 1
