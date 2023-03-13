import  random
import copy


class Proccess:
    def __init__(self ,id, arriving, length):
        self.id = id
        self.arriving = arriving
        self.length = length
        self.wait = 0
        self.finish = False
        self.response = None
    def __str__(self):
        return (f"Proccess(id ={self.id}, arriving = {self.arriving}, length= {self.length}, wait = {self.wait}," 
        f"finish = {self.finish}, reponse = {self.response})")
    
    def copy(self):
        newProcess = Proccess(self.id, self.arriving, self.length)
        newProcess.wait = self.wait
        newProcess.finish = self.finish
        newProcess.response = self.response
        return newProcess
def randomGeneratorProccesses()->list:
    arr = []
    for i in range(5):
        a = random.randint(1, 5)
        b= random.randint(1, 5)
        arr.append(Proccess(i,a, b))
    return arr

def putInWaitingQueue(proccesses: list[Proccess],waitingQueue: list, time: int ):
    for proccess in proccesses:
        if proccess.arriving <= time:
            waitingQueue.append(proccess)
            proccesses.remove(proccess)

def updateWaiting(waitingQueue: list[Proccess], wait: int):
    for proccess in waitingQueue:
        proccess.wait +=wait             

if __name__ == "__main__": 
    
    quantum = 2
    proccesses = randomGeneratorProccesses()
    length =  len(proccesses)
    schedule = {}
    running = None
    waitingQueue = []
    for proccess in proccesses:
        print(proccess)
        
    print("----------------------------------------------------------------------")
    finshed = 0 
    time = 0 
    adding = 0
    
    putInWaitingQueue(proccesses, waitingQueue, time)
    
    while True:
        if finshed == length: 
            break
        
        
        if len(waitingQueue)>0:
            running = waitingQueue.pop(0)
            if running.response is None:
                running.response = running.wait
            if running.length < quantum : 
                running.length = 0 
                running.finish = True
                time += 1
                adding =1
            else: 
                running.length -=quantum
                time += quantum
                adding = quantum
                if running.length ==0:
                    running.finish == True
        else:
            time +=1
            adding = 1
        
     
        updateWaiting(waitingQueue, adding)
        putInWaitingQueue(proccesses, waitingQueue, time)
        
        if running is None :
            continue
        
        schedule[time -adding] = running.copy() 
        
        if running.finish:
            finshed +=1
            
        if not running.finish:
            waitingQueue.append(running)
        
    print("Showing scheduling time of each proccess and their state after each quantum")
    for key, value in schedule.items():
        print (f"Time: {key} --> {value}")
        
    