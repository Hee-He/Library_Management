from PyQt6.QtWidgets import QWidget, QStackedWidget, QMessageBox
import mysql.connector as MC
from Database.config import config # Import the MainWindow class

class AddAccountWidget(QWidget):
    def __init__(self, parent, user, password):
        super().__init__()
        self.parent = parent
        self.add_account(user, password)

    def add_account(self, user, password):
        conn = None
        try:
            # Read the connection parameters
            params = config()
            
            # Connect to the MySQL server
            conn = MC.connect(**params)
            cur = conn.cursor(buffered=True)

            # Insert the new account into the users table
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (user, password)
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