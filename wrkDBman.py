from prettytable import PrettyTable
import os

clear = lambda: os.system('cls')

class Worker():
    def __init__(self, worker_tuple,  worker_id = None):
        self.name, self.position, self.salary = worker_tuple
        self.id = worker_id

    def __str__(self):
        display = PrettyTable()
        display.field_names = ["id", "name", "position", "salary"]
        display.add_row([self.id,self.name,self.position,self.salary])
        print(display)

    def edit(self):
        while(True):
            clear()
            self.__str__()
            print('Which position you want to change? (1 - Name | 2 - Position | 3 - Salary | 0 - Quit Editor')
            choose = int(input())
            if choose == 0:
                break
            elif choose == 1:
                clear()
                self.__str__()
                self.name = (input("Type new name: ").upper())
            elif choose == 2:
                clear()
                self.__str__()
                self.position = (input("Type new position: ").upper())
            elif choose == 3:
                clear()
                self.__str__()
                self.salary = (int(input("Type new salary: ")))


    @property
    def returnTuple(self):
         return (self.name.upper(), self.position.upper(), self.salary)



def workerCreator():
    while(True):
        try:
            worker_params = (input("Name: "), input("Position: "), int(input("Salary: ")))
            break
        except:
            print('Uncorect data. Try again.')
    return Worker(worker_params)



