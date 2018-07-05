import helperDBman

class Menu():
    def start_M():
        helperDBman.clear()
        print('''
        1. NEW DATA BASE / OPEN EXISTING DATA BASE
        2. QUIT ''')

    def typeDBname_M():
        helperDBman.clear()
        print('''
        Type a name of database, if it already exist it will be open:

        NAME: ''')


    def main_M():
        helperDBman.clear()
        print('''
    	1. View all records.
    	2. Add records.
    	3. Update records.
    	4. Remove record.
    	5. Clear all.
    	6. Discard changes.
        7. Save.
    	8. Save and Quit.
    	9. Quit without saving. ''')

    def search_M():
        while(True):
            print('''
       	1. Search by ID.
       	2. Search by NAME.
        3. Cancel. ''')
            menu_choice = input()
            helperDBman.clear()
            if menu_choice == '1' :
                return 'id='+ input('Type employee row id: ').upper()
            elif menu_choice == '2' :
                return 'name="'+ input('Type employee name: ').upper() + '"'
            if menu_choice == '3' :
                helperDBman.displayInfo('Canceled.')
                return
            else:
                helperDBman.displayInfo('Wrong key.')
