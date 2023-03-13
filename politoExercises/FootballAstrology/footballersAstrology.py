
#retrieve data form zodiaco.csv file and create a dict with zodiac sign
def readZodiaco():
    dict = {}
    with open("FootballAstrology/zoidiaco.csv", "r") as file:
        for i in file.readlines() :
            arr =  i.strip().split(",")
            dict[arr[0]]= [arr[1] , arr[2]]
    return dict

# revesed date using mm/dd format and int convertion
def  dateConverter(str):
    strArr = str.split("/")
    date = int(strArr[1] + strArr[0])
    return date
# def read


#find zodiac sign accrding to the date 
def findZodiac(str):
    date = dateConverter(str)
    zodiac = readZodiaco()
    for key, value in zodiac.items():
        startDate , endDate = dateConverter(value[0]) , dateConverter(value[1])
        if (date>=startDate and date<=endDate):
            return key
    # this is the only  option out of order of rule followed for finding zodiac sign
    # Capricorn,22/12,20/01        
    return "Capricorn"

#function to create the dictinary with zodiac signs and calculatin goals for each sign 
def goalCalculation():
    goalsDict = {}
    with open("FootballAstrology/sportivi.csv", "r") as file:
        for line in file.readlines():
            array = line.strip().split(",")
            zodiac = findZodiac(array[3])
            if zodiac in goalsDict:
                goalsDict[zodiac] = goalsDict[zodiac] + int(array[1])
            else :
                goalsDict[zodiac] = int(array[1])
    return goalsDict


def main():
    
    # method to sort dictionary 
    goalOrderDict = dict(sorted(goalCalculation().items() , key = lambda x : x[1] , reverse=True))
    
    # calculate delimeter on that way not to exide 50 stars
    delimeter = int(list(goalOrderDict.values())[0] / 50)
    
    for key,  value in goalOrderDict.items() :
        print(key, value, int(value/delimeter)*"*" )
   


if __name__== "__main__" :
    main()
