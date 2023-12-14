from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import mysql.connector as MC
from Database.config import config

class Details(QWidget):
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
        group_box = QGroupBox("Borrow Books",self)
        group_box.setGeometry(500,300,500,300)
        self.printdata = QPushButton("push",group_box)
        self.printdata.clicked.connect(self.print_selected_items)
        self.username_entry = QLineEdit(group_box)
        self.username_entry.setPlaceholderText("Student name")

        self.booklist = set()
        self.facultylbl = QLabel("Select Faculty: ",self)
        self.faculty = QComboBox(group_box)


        # Add items to the self.faculty
        self.faculty.addItem("Select faculty")
        self.faculty.addItem("BCA")
        self.faculty.addItem("BIM")
        self.faculty.addItem("BBA")
        self.faculty.addItem("BBS")
        self.faculty.addItem("Bsc. Csit")

        self.faculty.currentIndexChanged.connect(self.on_dropdown_changed)
        
        self.semlbl = QLabel("Select Semester: ",group_box)
        self.semester = QComboBox(group_box)

        # Add items to the self.semester
        self.semester.addItem("Select Sem")
        self.semester.addItem("Sem 1")
        self.semester.addItem("Sem 2")
        self.semester.addItem("Sem 3")
        self.semester.addItem("Sem 4")
        self.semester.addItem("Sem 5")
        self.semester.addItem("Sem 6")
        self.semester.addItem("Sem 7")
        self.semester.addItem("Sem 8")

        # Connect a function to be called when the selection changes
        self.semester.currentIndexChanged.connect(self.on_dropdown_changed)

        self.booklbl = QLabel("No of books: ",group_box)
        self.NoOfBook = QComboBox()
        self.NoOfBook.setFixedSize(80,40)


        # Add items to the self.NoOfBook
        self.NoOfBook.addItem("No of book")
        self.NoOfBook.addItem("1")
        self.NoOfBook.addItem("2")
        self.NoOfBook.addItem("3")
        self.NoOfBook.addItem("4")
        self.NoOfBook.addItem("5")

        # Connect a function to be called when the selection changes
        self.NoOfBook.currentIndexChanged.connect(self.on_dropdown_changed)

    
        
        # self.createAcc.
        self.sign_up = QPushButton('Save',group_box)
        self.sign_up.setProperty("class",'signup')
        self.sign_up.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sign_up.clicked.connect(self.AddAcc)

        self.semester.currentIndexChanged.connect(self.update_list_widget)

        self.lst = []
        # Create a QListWidget
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(800,300,400,400)
        self.list_widget.hide()


    def update_list_widget(self, index):
        # Clear the existing items in the QListWidget
        self.list_widget.show()
        self.list_widget.clear()

        # Get the selected category from the QComboBox
        selected_category = self.semester.currentText()
        selected_item = self.faculty.currentText()

        # Add items to the QListWidget based on the selected category
        if selected_category == "Sem 1" and selected_item.upper() == "BCA":
            self.list_widget.addItems(["Book for BCA sem 1","\n","Math I", "Computer Fundamentals", "Digital Logic","Society And Technology","English I"])
            self.list_widget.itemClicked.connect(self.print_selected_items)
        elif selected_category == "Sem 2":
            self.list_widget.addItems(["Item 2A", "Item 2B", "Item 2C"])
        elif selected_category == "Sem 3":
            self.list_widget.addItems(["Item 3A", "Item 3B", "Item 3C"])

    def BackToLogin(self):
        self.stack.setCurrentIndex(0)

    def on_dropdown_changed(self, index):
        # This function will be called when the dropdown selection changes
        selected_option = self.sender().currentText()
        print(f"Selected Option: {selected_option}")

    def AddAcc(self):
        user = self.username_entry.text()
        faculty = self.faculty.currentText()
        sem = self.semester.currentText()
        noofbook = self.NoOfBook.currentText()
        if len(user)==0 or len(faculty)==0 or len(sem)==0 or len(noofbook)==0:
            QMessageBox.warning(self,'invalid',"Please enter all the details")
        else:
            from addDetails import AddDetails
            AddDetails(self,user,faculty,sem,noofbook,self.lst)
            
            self.stack.setCurrentIndex(1)
        self.list_widget.hide()
        self.username_entry.clear()
        self.booklist.clear()
        
    def print_selected_items(self,item):
        # Get the selected items from the QListWidget
        selected_items = [item.text() for item in self.list_widget.selectedItems()]
        self.booklist.update(selected_items)
        self.lst = list(self.booklist)

