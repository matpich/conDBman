from conDBman import Database as DB, tryToInt
import msvcrt, os, time, wrkDBman

x =os.path.isfile(os.getcwd()+'\\test_db.db')
print(x)

clear = lambda: os.system('cls')

def displayInfo(info):
    clear()
    print(info)
    time.sleep(1)

def areYouSure(condition):
    return True if condition.lower() == 'yes' else False

while(True):
    clear()
    print('''
    1. NEW DATA BASE / OPEN EXISTING DATA BASE
    2. QUIT ''')
    menu_choice = input()
    #menu_choice = msvcrt.getwch()
    if (menu_choice=='1'):
        clear()
        print('''
        Type a name of database, if it already exist it will be open:

NAME: ''')
        dataB = DB(input())
        dataB.createTable()
        clear()
    elif (menu_choice=='2'):
        break
    else:
        clear()
        print('No such option. Try again.')
        time.sleep(1)
    while(True):
        clear()
        print('''
    	1. View all records.
    	2. Add records.
    	3. Update records.
    	4. Remove record.
    	5. Clear all.
    	6. Discard changes.
    	7. Save and Quit.
    	8. Quit without saving. ''')

        menu_choice = input()
        #menu_choice = msvcrt.getwch()
        if(menu_choice=='1'):
            clear()
            dataB.readAllRecords()
            print('Press any key to continue')
            input()
            #msvcrt.getwch()
        elif(menu_choice=='2'):
            clear()
            dataB.addRecord(wrkDBman.workerCreator())
            displayInfo("Row added.")

        elif(menu_choice=='3'):
            clear()
            row_worker_info = dataB.searchValue(tryToInt(input('Type employee name or row id: ')))
            employee = wrkDBman.Worker(row_worker_info[1:], row_worker_info[0])
            employee.edit()

        elif(menu_choice=='4'):
            pass
        elif(menu_choice=='5'):
            if areYouSure(input("CLEAR TABLE: Type 'YES' if you want to proceed and press ENTER. Type anything else to cancel")):
                dataB.clearTable()
                displayInfo('Table cleared.')
        elif(menu_choice=='6'):
            if areYouSure(input("DISCARD CHANGES: Type 'YES' if you want to proceed and press ENTER. Type anything else to cancel.")):
                dataB.discardChanges();
                displayInfo('Discarding successful.')
            else:
                displayInfo("Canceled.")
        elif(menu_choice=='7'):
            dataB.saveQuit()
            break
        elif(menu_choice=='8'):
            dataB.discardQuit()
            break
        else:
            clear()
            print('No such option. Try again.')
            time.sleep(1)





