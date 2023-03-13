# read file and create a dict with kay player position and 
# value array of this position players
def readFile():
    dict = {}
    with open("Fantasy_Football/fantafoot.txt") as file:
        for line in file.readlines():
            array = line.strip().split(", ")
            if array[2] in dict :
                dict[array[2]].append({"surname":array[0] ,"team": array[1] , "value" : int(array[3])})
            else : 
                dict[array[2]] = [{"surname":array[0] ,"team": array[1] , "value" : int(array[3])}]
    return dict 

#this is the algorith that find player for specified position according 
#to the number of player and total amount spent for them
def findPlayers(position , money , i):
    byed= []
    players =readFile()[position] 
    players = sorted(players , key = lambda x:x["value"], reverse=True)
    for player in players:
        if (i-1==0):
            break
        if(player["value"] + i-1<=money):
            byed.append(player)
            money = money - player["value"] 
            i=i-1
    
    for j in range(1 , i+1):
        byed.append(players[len(players)-i])
    
    return byed


def main():
    goalKeepers = findPlayers("goalkeeper" , 20 , 3)
    defenders = findPlayers("defender" , 40 , 8) 
    midfielders = findPlayers("midfielder" , 80 , 8)
    forwards = findPlayers("forward", 120 , 6)

    print("Goalkeepers:" , end=" " )
    for el in goalKeepers:
        print(el["surname"] , el["value"] , end=" ")
    print()

    print("Defenders:" , end=" " )
    for el in defenders:
        print(el["surname"] , el["value"] , end=" ")
    print()

    print("Midfielders:" , end=" " )
    for el in midfielders:
        print(el["surname"] , el["value"] , end=" ")
    print()

    print("Forwards:" , end=" " )
    for el in forwards:
        print(el["surname"] , el["value"] , end=" ")


if __name__== "__main__" :
    main()