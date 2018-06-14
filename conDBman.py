import sqlite3
import os.path
from prettytable import PrettyTable, from_db_cursor

class Worker():
    def __init__(self, worker_tuple):
        self.id, self.name, self.position, self.salary = worker_tuple

    @property
    def returnTuple(self):
         return (self.name, self.position, self.salary)



class Database():
    def __init__(self,new_db_name, table_name = "clients"):
        self.db = sqlite3.connect('%s.db' % new_db_name)
        self.cur = self.db.cursor()
        self.table_name = table_name

    def createTable(self):
        try:
            self.cur.execute('CREATE TABLE %s (id integer primary key, name text, position text, salary real)' % self.table_name)
        except:
            pass

    def resetTable(self):
        self.cur.execute('DROP TABLE if exists %s' % self.table_name)
        self.createTable(table_name)

    def addRecord(self, record):
        self.cur.execute('INSERT INTO '+self.table_name+' (name, position, salary) VALUES (?, ?, ?)', record.returnTuple )

    def updateRecord(self, record):
        self.cur.execute('UPDATE '+self.table_name+
                         ' SET name="'+record.returnTuple[0]+'", position="'+record.returnTuple[1]+'", salary='+str(record.returnTuple[2])+
                         ' WHERE id='+str(record.id))


    def readAllRecords(self):
        self.cur.execute('SELECT * FROM %s' % self.table_name)
        self.display = from_db_cursor(self.cur) #loading rows into table from PrettyTable
        print(self.display) #displays Table

    def clearTable(self):
        self.cur.execute('DELETE FROM %s' % self.table_name)


    def stopDB(self):
        self.db.commit()
        self.db.close()





def main():
    dataB = Database("test_db")
    dataB.createTable()
##    dataB.updateRecord(Worker("Jim Beam", "No one", 4356))
    dataB.addRecord(Worker((18,"fyu", "Rock'n'fyu king", 10000)))
    dataB.readAllRecords()
    dataB.clearTable()
    input()
    dataB.stopDB()


main()

