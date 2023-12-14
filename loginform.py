from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import mysql.connector as MC
from Database.config import config

class LoginForm(QWidget):
    login_successful = pyqtSignal(str) 
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        qss = 'qss\\loginform.qss'
        with open(qss,'r') as f:
            self.setStyleSheet(f.read())
        # Create widgets
        self.group_box = QGroupBox(self)
        self.group_box.setTitle("Login")
        self.group_box.setGeometry(500,300,500,300)
        self.username_entry = QLineEdit(self.group_box)
        self.username_entry.move(50,50)
        self.username_entry.setPlaceholderText("Username")
        self.password_entry = QLineEdit(self.group_box)
        self.password_entry.move(50,100)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.createAcc = QPushButton("Create accout",self.group_box)
        self.createAcc.move(50,150)
        self.createAcc.clicked.connect(self.Acc)
        self.createAcc.setProperty("class",'create')
        self.createAcc.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button = QPushButton('Login',self.group_box)
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.move(50,200)
        self.login_button.setProperty("class",'login')
        

        # # Set up layout
        # layout = QVBoxLayout(self.group_box)
        # layout.addWidget(self.username_entry)
        # layout.addWidget(self.password_entry)
        # layout.addWidget(self.createAcc)
        # layout.addWidget(self.login_button)

        #  # Set the layout of the group box
        # self.group_box.setLayout(layout)

        # # Set the layout of the main widget
        # main_layout = QVBoxLayout(self)
        # main_layout.addWidget(self.group_box)

        # self.setLayout(main_layout)
        # Set up signal connections
        self.login_button.clicked.connect(self.login)


        
    def Acc(self):
        self.parent.show_create_page()
    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if len(username)==0 or len(password)==0:
            QMessageBox.warning(self,'invalid',"Please enter the username and password")

        else:
            conn = None
            try:
                # read the connection parameters
                params = config()
                # connect to the PostgreSQL server
                conn = MC.connect(**params)
                cur = conn.cursor(buffered=True)
                query = 'SELECT username,password FROM users WHERE username =\''+username+"\'"
                cur.execute(query)
                result=cur.fetchone()
                if result:
                    from ProfilePage import ProfileOf
                    ProfileOf(self,stack=None)
                    self.parent.show_main_page()
                else:
                    QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')
                    
                    
                    # close communication with the PostgreSQL database server
                cur.close()
                    

                        # commit the changes
                conn.commit()
            except (Exception, MC.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                self.uname  = self.username_entry.text()
                from ProfilePage import ProfileOf
                ProfileOf(self,stack=None)
                self.username_entry.clear()
                self.password_entry.clear()
        

