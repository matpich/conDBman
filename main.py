from conDBman import Database as DB
import msvcrt, os, time, wrkDBman

x =os.path.isfile(os.getcwd()+'\\test_db.db')
print(x)

clear = lambda: os.system('cls')


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
            msvcrt.getwch()
        elif(menu_choice=='2'):
            clear()

            dataB.addRecord(wrkDBman.Worker(("Jim Beam", "No one", 4356)))
            #clear()
            print('Row added.')
            time.sleep(1)
        elif(menu_choice=='3'):
            pass
        elif(menu_choice=='4'):
            pass
        elif(menu_choice=='5'):
            pass
        elif(menu_choice=='6'):
            pass
        elif(menu_choice=='7'):
            pass
        elif(menu_choice=='8'):
            break
        else:
            clear()
            print('No such option. Try again.')
            time.sleep(1)





