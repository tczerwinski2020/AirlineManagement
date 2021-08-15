# Author: Taylor Czerwinski
# Summer 2021


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from db_manager import DBManager

# Search for passenger based on ticket number
class Ticket_Number_Dialog(QDialog):
    # Constructor for Ticket_number_Dialog object
    def __init__(self, parent=None):  # parent is sent during instantiation
        super(Ticket_Number_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    # Sets up Ticket_Number_Dialog's attributes
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 545)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 40, 761, 441))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/airplane4.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(620, 500, 113, 32))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.close)
        self.exit.setAutoDefault(False)

        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.hide)
        self.back.setAutoDefault(False)

        self.search = QtWidgets.QLineEdit(Dialog)
        self.search.setGeometry(QtCore.QRect(390, 10, 113, 21))
        self.search.setObjectName("search")

        self.search.returnPressed.connect(self.search_ticket_number)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(179, 10, 161, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 50, 60, 16))
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(390, 50, 113, 21))
        self.name.setObjectName("name")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(270, 110, 101, 20))
        self.label_4.setObjectName("label_4")
        self.flight_number = QtWidgets.QLineEdit(Dialog)
        self.flight_number.setGeometry(QtCore.QRect(390, 80, 113, 21))
        self.flight_number.setObjectName("flight_number")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 80, 91, 20))
        self.label_5.setObjectName("label_5")
        self.departure_date = QtWidgets.QLineEdit(Dialog)
        self.departure_date.setGeometry(QtCore.QRect(390, 110, 113, 21))
        self.departure_date.setObjectName("departure_date")
        self.depart_time = QtWidgets.QLineEdit(Dialog)
        self.depart_time.setGeometry(QtCore.QRect(390, 210, 113, 31))
        self.depart_time.setObjectName("depart_time")
        self.arrival_time = QtWidgets.QLineEdit(Dialog)
        self.arrival_time.setGeometry(QtCore.QRect(570, 210, 113, 31))
        self.arrival_time.setObjectName("arrival_time")
        self.origin = QtWidgets.QLineEdit(Dialog)
        self.origin.setGeometry(QtCore.QRect(390, 250, 113, 21))
        self.origin.setObjectName("origin")
        self.destination = QtWidgets.QLineEdit(Dialog)
        self.destination.setGeometry(QtCore.QRect(570, 250, 113, 21))
        self.destination.setObjectName("destination")
        self.status = QtWidgets.QLineEdit(Dialog)
        self.status.setGeometry(QtCore.QRect(540, 160, 113, 21))
        self.status.setObjectName("status")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 160, 60, 16))
        self.label_6.setObjectName("label_6")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Translates Ticket_Number_Dialog's attributes to the user interface
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search Ticket Number"))
        self.exit.setText(_translate("Dialog", "Exit"))
        self.back.setText(_translate("Dialog", "Back"))
        self.label_2.setText(_translate("Dialog", "Search By Ticket Number:"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Departure Date"))
        self.label_5.setText(_translate("Dialog", "Flight Number"))
        self.label_6.setText(_translate("Dialog", "Status"))

    # Searches for a flight and passenger by ticket number
    def search_ticket_number(self):
        ticket_number = self.search.text()
        if ticket_number == "":
            return
        print("ticket Number:  " + ticket_number)
        db_manager = DBManager()
        record = db_manager.search_by_ticket_number(ticket_number)
        if record is None:
            return
        self.display_record(record)

    # Displays flight information and passenger information
    def display_record(self, record):
        print(record)
        self.name.setText(record[0][0])
        self.flight_number.setText(str(record[0][2]))
        self.departure_date.setText(record[0][1].strftime('%B %d,  %Y'))

        self.status.setText(record[1][5])
        self.depart_time.setText(record[1][3].strftime('%I:%M %p'))
        self.origin.setText(record[1][1])
        self.arrival_time.setText(record[1][4].strftime('%I:%M %p'))
        self.destination.setText(record[1][2])
