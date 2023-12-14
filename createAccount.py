from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import mysql.connector as MC
from Database.config import config

class CreateForm(QWidget):
    def __init__(self, parent,stack):
        super().__init__()

        self.parent = parent
        self.stack = stack
        self.init_ui()
        qss = 'qss\\createAccount.qss'
        with open(qss,'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        # Create widgets
        group_box = QGroupBox("Register",self)
        group_box.setGeometry(500,300,500,300)
        self.username_entry = QLineEdit(group_box)
        self.username_entry.setPlaceholderText("Username")
        self.password_entry = QLineEdit(group_box)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.username_entry.move(50,50)
        self.password_entry.move(50,100)
        
        # self.createAcc.
        self.sign_up = QPushButton('Sign Up',group_box)
        self.sign_up.setProperty("class",'signup')
        self.sign_up.move(50,150)
        self.sign_up.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sign_up.clicked.connect(self.AddAcc)
        self.login_button = QPushButton('Back to login',group_box)
        self.login_button.setProperty("class",'login')
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.clicked.connect(self.BackToLogin)
        self.login_button.move(50,200)





    def BackToLogin(self):
        self.stack.setCurrentIndex(0)


    def AddAcc(self):
        user = self.username_entry.text()
        passwd = self.password_entry.text()
        if len(user)==0 or len(passwd)==0:
            QMessageBox.warning(self,'invalid',"Please enter the username and password")
        else:
            from addAccount import AddAccountWidget
            AddAccountWidget(self,user,passwd)
            self.stack.setCurrentIndex(0)

        self.username_entry.clear()
        self.password_entry.clear()
        
