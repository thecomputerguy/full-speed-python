import sqlite3

class DataConn():

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """ connect to sqllite """
        self.conn = sqlite3.Connection(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """ close the connection """
        self.conn.close()
        if exc_val:
            raise
    

if __name__ == "__main__":
    db_name = "airbnb.db"
    with DataConn(db_name) as connection:
        cursor = connection.cursor()
        print(cursor)




