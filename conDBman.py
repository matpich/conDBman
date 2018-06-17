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
            self.cur.execute('CREATE TABLE %s (id integer primary key, name text, position text, salary real)' % self.table_name)
        except:
            pass

    #require Worker object
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

    def deleteRow(self, id_number):
        self.cur.execute('DELETE FROM '+self.table_name+' WHERE id='+str(id_number))

    #this method is looking for employee in database using id or name. If there is to many matches it asks user to type an id. If only one row is find in DB it returns it as a tuple which will be used to define "Worker" class object.
    def searchValue(self,condition):
        if type(condition).__name__ == 'str':
            condition = 'name="'+condition.upper()+'"'
        else:
            condition = 'id='+str(condition) #if input value is string (name) then condition is set to name="value", when input is integer then id=value
        self.cur.execute('SELECT * FROM {} WHERE {}'.format(self.table_name, condition))
        #it was imposible to use "from_db_cursor" like in readAllRecords method because I was unable to return the number of rows returned by that function
        self.display = PrettyTable()
        self.display.field_names = ["id", "name", "position", "salary"]
        counter = 0
        row_info = ()
        for row in self.cur.fetchall():
            self.display.add_row(row)
            counter += 1
            row_info = row
        print(self.display) #displays Table
        if counter>1:
            print('To many matches, try to find by id.\nPress any key to continue.')
            input()
        else:
            return None if row_info == () else row_info

    def saveQuit(self):
        self.db.commit()
        self.db.close()

    def discardChanges(self):
        self.db.rollback()

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

