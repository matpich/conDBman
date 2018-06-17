from conDBman import Database as DB
import msvcrt, os, time, wrkDBman, helperDBman

x =os.path.isfile(os.getcwd()+'\\test_db.db')
print(x)


sure_info ="Type 'YES' if you want to proceed and press ENTER. \nType anything else to cancel."

while(True):
    helperDBman.clear()
    print('''
    1. NEW DATA BASE / OPEN EXISTING DATA BASE
    2. QUIT ''')
    #menu_choice = input()
    menu_choice = msvcrt.getwch()
    if (menu_choice=='1'):
        helperDBman.clear()
        print('''
        Type a name of database, if it already exist it will be open:

        NAME: ''')
        dataB = DB(input())
        dataB.createTable()
        helperDBman.clear()

        while(True):
            helperDBman.clear()
            print('''
        	1. View all records.
        	2. Add records.
        	3. Update records.
        	4. Remove record.
        	5. Clear all.
        	6. Discard changes.
        	7. Save and Quit.
        	8. Quit without saving. ''')

            #menu_choice = input()
            menu_choice = msvcrt.getwch()
            if(menu_choice=='1'):
                helperDBman.clear()
                dataB.readAllRecords()
                print('Press any key to continue')
                #input()
                msvcrt.getwch()
            elif(menu_choice=='2'):
                helperDBman.clear()
                dataB.addRecord(wrkDBman.workerCreator())
                helperDBman.displayInfo("Row added.")

            elif(menu_choice=='3'):
                helperDBman.clear()
                row_worker_info = dataB.searchValue(helperDBman.int_or_str(input('Type employee name or row id: ')))
                if row_worker_info == None:
                    continue
                else:
                    pass
                employee = wrkDBman.Worker(row_worker_info[1:], row_worker_info[0])
                employee.edit()
                if helperDBman.areYouSure(input("UPDATE ROW: "+sure_info)):
                    dataB.updateRecord(employee)
                    helperDBman.displayInfo('Row updated.')
                else:
                    helperDBman.displayInfo('Updating cancelled.')

            elif(menu_choice=='4'):
                helperDBman.clear()
                row_worker_info = dataB.searchValue(helperDBman.int_or_str(input('Type employee name or row id: ')))
                if row_worker_info == None:
                    continue
                else:
                    if helperDBman.areYouSure(input("DELETE ROW: "+sure_info)):
                        dataB.deleteRow(row_worker_info[0])
                        helperDBman.displayInfo("Row deleted.")
                    else:
                        helperDBman.displayInfo('Canceled.')
            elif(menu_choice=='5'):
                helperDBman.clear()
                if helperDBman.areYouSure(input("CLEAR TABLE: "+sure_info)):
                    dataB.clearTable()
                    helperDBman.displayInfo('Table cleared.')
            elif(menu_choice=='6'):
                helperDBman.clear()
                if helperDBman.areYouSure(input("DISCARD CHANGES: "+sure_info)):
                    dataB.discardChanges();
                    helperDBman.displayInfo('Discarding successful.')
                else:
                    helperDBman.displayInfo("Canceled.")
            elif(menu_choice=='7'):
                dataB.saveQuit()
                break
            elif(menu_choice=='8'):
                dataB.discardQuit()
                break
            else:
                helperDBman.displayInfo('No such option. Try again.')

    elif (menu_choice=='2'):
        break
    else:
        helperDBman.displayInfo('No such option. Try again.')