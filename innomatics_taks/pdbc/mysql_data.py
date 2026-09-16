
import mysql.connector as ms 
# Connect to MySQL
def mysqlabc():
    connection = ms.connect(
        host="localhost",
        user="root",
        password="a.vishnu@43499",
        database="pdbc_project"   
    )
    return connection

