def readFile():
    dict = {}
    with open("Bowling/bowling.txt", "r") as file:
        for line in file.readlines() :
            array  = line.strip().split(";")
            name = " ".join([array[0] ,array[1]]) 
            score = [int(x) for x  in array[2 : len(array)]]
            total_score  = sum(score)
            tenPoint = score.count(10)
            zeroPoint = score.count(0)
            dict[name] = [total_score , tenPoint , zeroPoint]    
    return dict

def mostTenPointFinder():
    scoreOrdered =  dict(sorted(readFile().items() , key= lambda x : x[1][1] , reverse=True))
    name , score  = list(scoreOrdered.items())[0][0]  , list(scoreOrdered.items())[0][1][1] 
    return name, score

def mostZeroPointFinder():
    scoreOrdered =  dict(sorted(readFile().items() , key= lambda x : x[1][2] , reverse=True))
    name , score  = list(scoreOrdered.items())[0][0]  , list(scoreOrdered.items())[0][1][2] 
    return name, score

def main():
    scoreOrdered =  dict(sorted(readFile().items() , key= lambda x : x[1][0] , reverse=True))
    for key ,value in scoreOrdered.items():
       print (key , value[0] )
    name , score= mostTenPointFinder()
    print ("{0} has knocked down all the pins {1} times".format(name , score))
    name , score= mostZeroPointFinder()
    print ("{0} has missed all the pins {1} times".format(name , score))

    
if __name__== "__main__" :
    main()