
#This is the function  that take inputs from the input file 
# after that create a player dictionary with player data
# and an array of demon dictionary with all demons data 
# 2 additional data for the demon stamina gain and total rewards 
# according to turns remainded after attacking the user
def readFile():
    dict = {}
    demons = []
    with open("input.txt", "r") as file:
      
        firstline  =[ int (x) for x in file.readline().split()]
       
        player = {
                "S":firstline[0], 
                "S_max" : firstline[1],
                "T":firstline[2] ,
                "Dem":firstline[3] 
                }

        for line in file.readlines() :
            
            array  =  [int(x) for x in line.strip().split()]
            demon= {
                "S_dam":array[0], 
                "T" : array[1], 
                "S_rec" : array[2], 
                "Na" : array[3] , 
                "A" : array[4:len(array)],
                "S_gain" : array[2]- array[0]
            }

            Reword(player["T"], demon)
            
            demons.append(demon)


    return player , demons


# function that calculate the rewards after attacking each demon 
# according to the player turns  
def Reword(turns , demon):
    turns  = turns - demon["T"]
    if (turns > len(demon["A"])):
        reword = sum(demon["A"])
    else:
        reword = sum(demon["A"][0:turns])
    demon["R"]= reword

#this function decide which demon is going to be attacked first 
# according to the total gain and best rewards 
def attackFist(demons):
    best = demons[0]
    for demon in demons[1:len(demons)]:
        if(demon["S_gain"]+ demon["R"] >best["S_gain"]+ best["R"] ):
            best = demon
    return best

#This is the function that decide the order of demons to be attacked
#Each time check if we have enought stamina then filter according to the function up
#For each attacked demon keep track of stamina and rewards
def Attack(player , demons):
    rewards = 0 
    T_init = player["T"]
    S_max = player["S_max"]
    nr_dem = player["Dem"]
    order = []
    demons_init = [demon for demon in demons]
    print("-----------Stamina---------" , player["S"], "-----Initial-----Rewards" , rewards)
    for i in range(0, nr_dem):
        fitered = []
        for demon in demons:
            if(player["S"] > demon["S_dam"]):
                fitered.append(demon)
        attack_dem = attackFist(fitered) 
        index = demons_init.index(attack_dem)
        order.append(index)
        if (attack_dem["S_gain"] + player["S"] >= S_max ):
            player["S"] = S_max
        else : 
             player["S"] = attack_dem["S_gain"] + player["S"]
        demons.remove(attack_dem)
        rewards =rewards + attack_dem["R"]
        print("-----------Stamina---------" , player["S"], "----After attacking" , index , "-----Rewards" , rewards)
   
    return order




if __name__== "__main__" :
    player , demons = readFile() ;
    print("Player ----------------------------------------------------------------------")
    for key in player.keys():
        print(key , player[key])
    print("////////////////////////////////////////////////////////////////////////")
    i = 1
    for demon in demons:
        print("Demon", i, "----------------------------------------------------------------------")
        for key in demon : 
            print(key , demon[key])
        i +=1
    order  = Attack(player , demons)

    print("Order is: " , *order)

    file = open("output.txt", "w")
    for el in order :
        file.write("{0}\n".format(el))
    file.close()