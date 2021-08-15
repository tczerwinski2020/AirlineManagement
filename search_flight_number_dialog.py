# Author: Taylor Czerwinski
# Summer 2021


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from db_manager import DBManager

# Search for flight by flight number
class Flight_Number_Dialog(QDialog):
    # Constructs instance of a Flight_Number_Dialog object
    def __init__(self, parent=None):  # parent is sent during instantiation
        super(Flight_Number_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    # Sets up Flight_Number_Dialog's attributes
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(763, 494)
        self.picture = QtWidgets.QLabel(Dialog)
        self.picture.setGeometry(QtCore.QRect(0, 50, 761, 381))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("Images/airplane5.webp"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.close)
        self.back.setAutoDefault(False)

        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(640, 450, 113, 32))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.close)
        self.exit.setAutoDefault(False)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 151, 20))
        self.label.setObjectName("label")
        self.search = QtWidgets.QLineEdit(Dialog)
        self.search.setGeometry(QtCore.QRect(350, 10, 151, 21))
        self.search.setObjectName("search")
        self.search.returnPressed.connect(self.search_flight_number)
        self.employees = QtWidgets.QTableWidget(Dialog)
        self.employees.setGeometry(QtCore.QRect(10, 290, 311, 131))
        self.employees.setObjectName("employees")
        self.employees.setColumnCount(2)
        self.employees.setRowCount(0)
        self.employees.setColumnWidth(0, 155)
        self.employees.setColumnWidth(1, 155)
        self.employees.setHorizontalHeaderLabels(
            ["Employee Name", "Employee Number"])

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.flight_number = QtWidgets.QLineEdit(Dialog)
        self.flight_number.setGeometry(QtCore.QRect(230, 260, 81, 21))
        self.flight_number.setObjectName("flight_number")
        self.passengers = QtWidgets.QTableWidget(Dialog)
        self.passengers.setGeometry(QtCore.QRect(430, 290, 321, 131))
        self.passengers.setObjectName("passengers")
        self.passengers.setColumnCount(2)
        self.passengers.setRowCount(0)
        self.passengers.setColumnWidth(0, 155)
        self.passengers.setColumnWidth(1, 155)
        self.passengers.setHorizontalHeaderLabels(
            ["Passenger Name", "Ticket Number"])

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 260, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.flight_number2 = QtWidgets.QLineEdit(Dialog)
        self.flight_number2.setGeometry(QtCore.QRect(600, 260, 91, 21))
        self.flight_number2.setObjectName("flight_number2")
        self.origin = QtWidgets.QLineEdit(Dialog)
        self.origin.setGeometry(QtCore.QRect(400, 120, 113, 21))
        self.origin.setObjectName("origin")
        self.depart_time = QtWidgets.QLineEdit(Dialog)
        self.depart_time.setGeometry(QtCore.QRect(400, 70, 111, 41))
        self.depart_time.setObjectName("depart_time")
        self.arrival_time = QtWidgets.QLineEdit(Dialog)
        self.arrival_time.setGeometry(QtCore.QRect(540, 70, 111, 41))
        self.arrival_time.setObjectName("arrival_time")
        self.destination = QtWidgets.QLineEdit(Dialog)
        self.destination.setGeometry(QtCore.QRect(540, 120, 113, 21))
        self.destination.setObjectName("destination")
        self.depart_date = QtWidgets.QLineEdit(Dialog)
        self.depart_date.setGeometry(QtCore.QRect(110, 70, 113, 21))
        self.depart_date.setObjectName("depart_date")
        self.status = QtWidgets.QLineEdit(Dialog)
        self.status.setGeometry(QtCore.QRect(110, 120, 113, 21))
        self.status.setObjectName("status")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Translates Flight_Number_Dialog's attributes to the user interface
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Flight Number"))
        self.back.setText(_translate("Dialog", "Back"))
        self.exit.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Look Up Flight Number: "))
        self.label_2.setText(_translate("Dialog", "Employees  Working Flight:"))
        self.label_3.setText(_translate("Dialog", "Passengers On Flight:"))

    # Retrieves a flight's record, passengers and employees, by searching for a flight number
    def search_flight_number(self):
        flight_number = self.search.text()
        if flight_number == "":
            return
        print("flight Number:  " + flight_number)
        db_manager = DBManager()
        flight_record = db_manager.get_flight_info(flight_number)
        if flight_record is None:
            return
        employees_assigned = db_manager.get_employees_assigned(flight_number)
        employees = []
        for employee in employees_assigned:
            name = db_manager.get_employee_name(employee[0])
            name = name[0].replace("[()]", "")
            depart_date = employee[1]
            temp = [employee[0], name]
            employees.append(temp)
        passengers = db_manager.get_passengers(flight_number, depart_date)
        self.display_record(flight_record, employees, depart_date, passengers)

    # Displays a flight's record, passengers, and employees
    def display_record(self, flight_record, employees, depart_date, passengers):
        self.status.setText(flight_record[5])
        self.depart_time.setText(flight_record[3].strftime('%I:%M %p'))
        self.arrival_time.setText(flight_record[4].strftime('%I:%M %p'))
        self.origin.setText(flight_record[1])
        self.destination.setText(flight_record[2])
        self.flight_number.setText(str(flight_record[0]))
        self.flight_number2.setText(str(flight_record[0]))
        self.depart_date.setText(depart_date.strftime('%B %d,  %Y'))

        num_rows = len(employees)
        self.employees.setRowCount(num_rows)
        table_row = 0
        for row in employees:
            self.employees.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.employees.setItem(table_row, 1, QtWidgets.QTableWidgetItem(str(row[0])))
            table_row += 1

        num_rows = len(passengers)
        self.passengers.setRowCount(num_rows)
        table_row = 0
        for row in passengers:
            self.passengers.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.passengers.setItem(table_row, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            table_row += 1
