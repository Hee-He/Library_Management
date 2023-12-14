from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class ProfileOf(QWidget):

    def __init__(self,parent,stack):
        super().__init__()
        self.stack = stack
        self.parent = parent


       

        self.borrow = QPushButton("Borrow Book",self)
        self.borrow.clicked.connect(self.setProf)
        self.returnBook = QPushButton("Return Book",self)
        self.returnBook.clicked.connect(self.returnbook)
        self.logout_button = QPushButton('Logout',self)

        # Set up signal connections
        self.logout_button.clicked.connect(self.confirm_logout)


    def returnbook(self):
        self.parent.show_return_books()
    
    def setProf(self):
        self.parent.show_profile_page()


    def confirm_logout(self):
        reply = QMessageBox.question(self, 'Logout Confirmation', 'Are you sure you want to logout?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.logout()

    def logout(self):
        self.parent.show_login_page()

    