import sqlite3
import os.path
import helperDBman
from prettytable import PrettyTable, from_db_cursor



class Database():
    def __init__(self,new_db_name, table_name = "clients"):
        self.db = sqlite3.connect('%s.db' % new_db_name)
        self.cur = self.db.cursor()
        self.table_name = table_name

    def createTable(self):
        try:
            self.cur.execute('CREATE TABLE {} (id integer primary key, name text, position text, salary real)'.format(self.table_name))
        except:
            pass

    #require Worker object
    def addRecord(self, record):
        self.cur.execute('INSERT INTO {} (name, position, salary) VALUES (?, ?, ?)'.format(self.table_name), record.returnTuple )
        helperDBman.displayInfo("Row added.")

    def updateRecord(self, record):
        self.cur.execute('UPDATE {} SET name=?, position=?, salary=? WHERE id=?'.format(self.table_name),(record.returnTuple[0],record.returnTuple[1],str(record.returnTuple[2]),str(record.id)))
        helperDBman.displayInfo('Row updated.')

    def readAllRecords(self):
        self.cur.execute('SELECT * FROM {}'.format(self.table_name))
        helperDBman.displayTable(self.cur.fetchall())

    def clearTable(self):
        self.cur.execute('DELETE FROM {}'.format(self.table_name))
        helperDBman.displayInfo('Table cleared.')

    def deleteRow(self, id_number):
        self.cur.execute('DELETE FROM {} WHERE id=?'.format(self.table_name), (id_number,))
        helperDBman.displayInfo("Row deleted.")

    def searchValue(self,condition):
        if condition is None:
            return
        self.cur.execute('SELECT * FROM {} WHERE {}'.format(self.table_name, condition))
        rows = self.cur.fetchall()
        if len(rows)>1:
            helperDBman.displayTable(rows)
            print('To many matches, try to find by id.\nPress any key to continue.')
            input()
        elif rows == []:
            helperDBman.displayInfo('Record not found.')
            return None
        else:
            return rows[0]

    def saveQuit(self):
        self.db.commit()
        self.db.close()

    def save(self):
        self.db.commit()
        helperDBman.displayInfo('Saving successful.')

    def discardChanges(self):
        self.db.rollback()
        helperDBman.displayInfo('Discarding successful.')

    def discardQuit(self):
        self.db.rollback()
        self.db.close()





def main():
    pass
##    dataB = Database("a")
##    dataB.searchValue(helperDBman.int_or_str(input()))
######    dataB.updateRecord(Worker("Jim Beam", "No one", 4356))
##    dataB.addRecord(Worker((18,"Karol", "Ogarniacz", 10000)))
##    #dataB.readAllRecords()
####    dataB.clearTable()
####    input()
####    dataB.stopDB()


main()

