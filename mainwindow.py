from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from loginform import LoginForm
from ProfilePage import ProfileOf
from createAccount import CreateForm
from addAccount import AddAccountWidget
from createDetails import Details
from returnBook import ReturnBook
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        qss = 'qss\\mainwindow.qss'
        with open(qss,'r') as f:
            self.setStyleSheet(f.read())


        
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setGeometry(0,0,1000,1000)
        self.login_page = LoginForm(self)
        self.create_page = CreateForm(self,self.stacked_widget)
        self.main_page = ProfileOf(self,stack=self.stacked_widget)
        self.set_details = Details(self,stack=self.stacked_widget)
        self.return_book = ReturnBook(self)

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.create_page)
        self.stacked_widget.addWidget(self.set_details)
        self.stacked_widget.addWidget(self.return_book)
        self.init_ui()

    def init_ui(self):
        # Set the main layout for the window
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.stacked_widget)
        # self.setLayout(layout)

        self.setWindowTitle('FunTus')
        self.setWindowIcon(QIcon("Program_icon\\chat-icon-png_302635.jpg"))

        self.setWindowState(Qt.WindowState.WindowMaximized)


    def show_login_page(self):
        self.stacked_widget.setCurrentWidget(self.login_page)

    def show_main_page(self):
        self.stacked_widget.setCurrentWidget(self.main_page)
    
    def show_create_page(self):
        self.stacked_widget.setCurrentWidget(self.create_page)
    
    def show_profile_page(self):
        self.stacked_widget.setCurrentWidget(self.set_details)

    def show_return_books(self):
        self.stacked_widget.setCurrentWidget(self.return_book)