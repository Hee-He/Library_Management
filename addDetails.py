from PyQt6.QtWidgets import *
import mysql.connector as MC
from Database.config import config # Import the MainWindow class

class AddDetails(QWidget):
    def __init__(self, parent, user, faculty,sem,noofbook,booklist):
        super().__init__()
        self.parent = parent
        self.add_account(user, faculty,sem,noofbook,booklist)

    def add_account(self, user, faculty,sem,noofbook,booklist):
        conn = None
        try:
            # Read the connection parameters
            params = config()
            
            # Connect to the MySQL server
            conn = MC.connect(**params)
            cur = conn.cursor(buffered=True)
            book1= booklist[0]
            book2= booklist[1]
            book3= booklist[2]
            print(book1,book2,book3)
            # Insert the new account into the users table
            sql = "INSERT INTO students (name,faculty,semester,book1,book2,book3) VALUES (%s, %s,%s,%s,%s,%s)"
            values = (user, faculty,sem,book1,book2,book3)
            cur.execute(sql, values)

            # Commit the changes
            conn.commit()
            QMessageBox.information(self, "Success", "Account created successfully.")

                    
                    
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