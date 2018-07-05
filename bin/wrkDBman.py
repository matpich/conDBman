from prettytable import PrettyTable
import os, msvcrt
import helperDBman


class Worker():
    def __init__(self, worker_tuple,  worker_id = None):
        self.name, self.position, self.salary = worker_tuple
        self.id = worker_id

    def edit(self):
        while(True):
            helperDBman.displayTable([(self.id, self.name.upper(), self.position.upper(), self.salary)])
            print('Which position you want to change? \n(1 - Name | 2 - Position | 3 - Salary | 0 - Quit Editor')
            choose = int(input())
            helperDBman.clear()
            if choose == 0:
                break
            elif choose == 1:
                self.name = (input("Type new name: ").upper())
            elif choose == 2:
                self.position = (input("Type new position: ").upper())
            elif choose == 3:
                self.salary = (helperDBman.tryToInt(input("Type new salary: ")))
            else:
                helperDBman.displayInfo('No such value, try again.')


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



