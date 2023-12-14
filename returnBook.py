from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import mysql.connector as MC
import sys
from Database.config import config

class ReturnBook(QWidget):
    def __init__(self,parent):
        super().__init__()


        self.name = QLineEdit(self)
        self.label = QLabel("Enter students name: ",self)
        self.label.setGeometry(20,20,200,30)
        self.name.setGeometry(40,20,100,50)
        self.name.setPlaceholderText("Students Name")
        self.name.returnPressed.connect(self.fetch_and_display_data)


    def fetch_and_display_data(self):
        # Execute the MySQL query to fetch all data from the user table
        name = self.name.text()
        try:
            # Read the connection parameters
            params = config()
            
            # Connect to the MySQL server
            conn = MC.connect(**params)
            cur = conn.cursor(buffered=True)
            # Insert the new account into the users table
            sql = 'SELECT * FROM students WHERE name =\''+name+"\'"
            cur.execute(sql)

            # Commit the changes
            conn.commit()
            # Fetch all rows from the result set
            rows = cur.fetchall()

            # Set the number of rows and columns in the table widget
            

            # Populate the table widget with data
            for row in rows:
                if row[0]!= None:
                    filtered_row = [str(x) for x in row if x is not None]
                    row_str = " \n ".join(filtered_row)
                    QLabel(row_str,self)
                else:
                    continue

                    
                    
            # close communication with the PostgreSQL database server
            cur.close()
                    

            # commit the changes
            conn.commit()
        except (Exception, MC.DatabaseError) as error:
            print(error)
            QMessageBox.critical(self, "Error", "Failed to create the account.")

        finally:
            if conn is not None:
                cur.close()
                conn.close()

