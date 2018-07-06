from conDBman import Database as DB
from menuDBman import Menu
import wrkDBman, helperDBman

def main():
    while(True):
        Menu.start_M()
        menu_choice = input()

        if (menu_choice=='1'):
            Menu.typeDBname_M()

            dataB = DB(input())
            dataB.createTable()

            while(True):
                Menu.main_M()
                menu_choice = input()
                helperDBman.clear()

                if(menu_choice=='1'):
                    dataB.readAllRecords()
                    print('Press any key to continue')
                    input()

                elif(menu_choice=='2'):
                    dataB.addRecord(wrkDBman.workerCreator())

                elif(menu_choice=='3'):
                    row_worker_info = dataB.searchValue(Menu.search_M())
                    if row_worker_info is None:
                       continue
                    employee = wrkDBman.Worker(row_worker_info[1:], row_worker_info[0])
                    employee.edit()
                    dataB.updateRecord(employee) if helperDBman.areYouSure(input("UPDATE ROW: "+Menu.sure_info)) else helperDBman.displayInfo('Cancelled.')

                elif(menu_choice=='4'):
                    row_worker_info = dataB.searchValue(Menu.search_M())
                    if row_worker_info is None:
                        continue
                    dataB.deleteRow(row_worker_info[0]) if helperDBman.areYouSure(input("DELETE ROW: "+Menu.sure_info)) else helperDBman.displayInfo('Cancelled.')

                elif(menu_choice=='5'):
                    dataB.clearTable() if helperDBman.areYouSure(input("CLEAR TABLE: "+Menu.sure_info)) else helperDBman.displayInfo('Cancelled.')

                elif(menu_choice=='6'):
                    dataB.discardChanges() if helperDBman.areYouSure(input("DISCARD CHANGES: "+Menu.sure_info)) else helperDBman.displayInfo("Cancelled.")

                elif(menu_choice=='7'):
                    dataB.save()

                elif(menu_choice=='8'):
                    dataB.saveQuit()
                    break

                elif(menu_choice=='9'):
                    dataB.discardQuit()
                    break
                else:
                    helperDBman.displayInfo('No such option. Try again.')

        elif (menu_choice=='2'):
            helperDBman.clear()
            break
        else:
            helperDBman.displayInfo('No such option. Try again.')

main()