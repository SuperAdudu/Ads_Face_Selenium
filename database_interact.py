import pyodbc
import time
from datetime import datetime
# Biến dùng để kết nối database
xml_file_path_database = "E:\\Project_Python\\facebookBot\\Database_V3.accdb"
con_string = (
        r'DRIVER= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + xml_file_path_database + ";")
class Log_FacebookBot:
    def __init__(self, Account, TimeAction,Content, Action, Status, Group):
        self.Account = Account
        self.TimeAction = TimeAction
        self.Content = Content
        self.Action = Action
        self.Status = Status
        self.Group = Group
    def saveDB(self):
        conn = pyodbc.connect(con_string)
        #start_time = time.time()
        cursor = conn.cursor()
        insert_query = """
                        INSERT INTO Log_FacebookBot 
                        (Account, TimeAction,[Content], Action, Status, [Group])
                        VALUES (?, ?, ?, ?, ?, ?)
                        """
        cursor.execute(insert_query, (self.Account, self.TimeAction,self.Content, self.Action,
                                      self.Status, self.Group))
        conn.commit()
        cursor.close()
        conn.close()