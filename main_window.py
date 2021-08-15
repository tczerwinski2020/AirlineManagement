# Author: Taylor Czerwinski
# Summer 2021

from search_ticket_number_dialog import Ticket_Number_Dialog
from search_flight_number_dialog import Flight_Number_Dialog
from search_by_date_dialog import Date_Dialog
from search_employee_no_dialog import Employee_No_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

# Main Window class
class Ui_MainWindow(QMainWindow):
    # Creates an instance of Ui_MainWindow
    def __init__(self):
        # This is needed here to inherit methods and data from QMainWindow
        super(Ui_MainWindow, self).__init__()
        self._system_name = "Airline Management System"
        self.setupUi(self)  # This method was provided by PyQt Designer. Note the snake_case update
        self.retranslateUi(self)  # This method was provided by PyQt Designer. Note the snake_case update

    # Set up Ui_MainWindow's attributes
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(752, 535)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(0, 0, 751, 391))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("Images/airplane.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.flight_number = QtWidgets.QPushButton(self.centralwidget)
        self.flight_number.setGeometry(QtCore.QRect(190, 430, 171, 32))
        self.flight_number.setObjectName("flight_number")
        self.flight_number.clicked.connect(self.open_flight_number)

        self.ticket_number = QtWidgets.QPushButton(self.centralwidget)
        self.ticket_number.setGeometry(QtCore.QRect(10, 430, 171, 32))
        self.ticket_number.setObjectName("ticket_number")
        self.ticket_number.clicked.connect(self.open_ticket_number)
        self.dates = QtWidgets.QPushButton(self.centralwidget)
        self.dates.setGeometry(QtCore.QRect(370, 430, 161, 32))
        self.dates.setObjectName("dates")
        self.dates.clicked.connect(self.open_dates)

        self.employee_number = QtWidgets.QPushButton(self.centralwidget)
        self.employee_number.setGeometry(QtCore.QRect(540, 430, 191, 32))
        self.employee_number.setObjectName("employee_number")
        self.employee_number.clicked.connect(self.open_employee_no)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(620, 480, 113, 32))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 320, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(251, 253, 252)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Translates Ui_MainWindow's attributes to user interface
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB_Airways"))
        self.flight_number.setText(_translate("MainWindow", "Look Up Flight Number"))
        self.ticket_number.setText(_translate("MainWindow", "Look Up Ticket Number"))
        self.dates.setText(_translate("MainWindow", "Look Up Dates"))
        self.employee_number.setText(_translate("MainWindow", "Look Up Employee Number"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "𝘿𝘽_𝘼𝙞𝙧𝙬𝙖𝙮𝙨"))

    # Opens Ticket_Number_Dialog
    def open_ticket_number(self):
        dialog = Ticket_Number_Dialog()
        dialog.exec_()
        dialog.show()

    # Opens Flight_Number_Dialog
    def open_flight_number(self):
        dialog = Flight_Number_Dialog()
        dialog.exec_()
        dialog.show()

    # Opens Date_Dialog
    def open_dates(self):
        dialog = Date_Dialog()
        dialog.exec_()
        dialog.show()

    # Opens Employee_No_Dialog
    def open_employee_no(self):
        dialog = Employee_No_Dialog()
        dialog.exec_()
        dialog.show()
