class Worker():
    def __init__(self, worker_tuple):
        self.name, self.position, self.salary = worker_tuple

##    def __str__(self):
##        return "Name: " + self.name + " Position: " + self.position + " Salary: " + str(self.salary)

    @property
    def returnTuple(self):
         return (self.name, self.position, self.salary)



def workerCreator():
    while(True):
        try:
            worker_params = (input("Name: "), input("Position: "), int(input("Salary: ")))
            break
        except:
            print('Uncorect data. Try again.')
    return Worker(worker_params)



