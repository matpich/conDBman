import os, time

clear = lambda: os.system('cls')

def displayInfo(info, sleep_time=1):
    clear()
    print(info)
    time.sleep(sleep_time)
    clear()


def displayTable(rows):
    print("ID | NAME | POSITION | SALARY")
    for row in rows:
        print(str(row[0]) + ' | ' + row[1] + ' | '+ row[2] + ' | '+ str(row[3]))


def tryToInt(string_or_int):
    while(True):
        try:
            int(string_or_int)
            return int(string_or_int)
        except:
            print("Wrong value. Try again.")
            string_or_int = input("Type new salary: ")

def areYouSure(condition):
    return True if condition.lower() == 'yes' else False