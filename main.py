# This is a sample Python script.
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from GUI.LoginForm import LoginRegisterWindow
from Utils import cypher


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.validUser = False
        self.login_form: LoginRegisterWindow = LoginRegisterWindow()
        self.user_credentials = None
        self.credentials()
        print(self.user_credentials)

    def credentials(self):
        self.login_form.show()
        #       print(self.login_form.exec_()) print 1 on success, 0 on reject.
        if self.login_form.exec_() == 1:
            self.login_form.result["password"] = cypher(self.login_form.result["password"])
            self.user_credentials = self.login_form.result
        else:
            sys.exit(0)


# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = UI()

    app.exec()
