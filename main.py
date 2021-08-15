# Author: Taylor Czerwinski
# Summer 2021

from db_manager import DBManager
from main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
import sys

def main():
    db_manager = DBManager()

    app = QApplication(sys.argv)
    ui = Ui_MainWindow()  # creates an instance of the MainUI
    ui.show()
    sys.exit(app.exec())
      # Press ⌘F8 to toggle the breakpoint.



main()
