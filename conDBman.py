import sqlite3
import os.path

class Worker():
    def __init__(self, name, position, salary):
        self.name, self.position, self.salary = name, position, salary



class Database():
    def __init__(self,new_db_name):
        self.db = sqlite3.connect('%s.db' % new_db_name)
        self.cur = self.db.cursor()

    def createTable(self,table_name):
        try:
            self.cur.execute('create table %s (name text, position text, salary real)' % table_name)
        except:
            print("Table already exist, if you want to override it use 'overrideTable' function.")

    def overrideTable(self,table_name):
        self.cur.execute('drop table if exists %s' % table_name)
        self.createTable(table_name)

    def addColumn(self,table_name, column_name, data_type):
        self.cur.execute('alter table %s add %s %s' % (table_name,column_name,data_type))

    def stopDB(self):
        self.db.commit()
        self.db.close()

    def addRecord(self, table_name, record):
        self.cur.execute("INSERT INTO "+table_name+" VALUES (?,?,?,?)", record)





def main():
    dataB = Database("test_db")
    dataB.overrideTable("clients")
    dataB.addColumn("clients","email","text")
    dataB.addRecord("clients",("asd","fad",89,"gf"))
    dataB.stopDB()

main()

