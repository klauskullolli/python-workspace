
def readFile():
    list= []
    with open("Guess_Who/characters.txt") as file:
        array = file.readline().strip().split("; ")
        for line in file.readlines():
            array2 = line.strip().split("; ")
            dict = {}
            for i in range(0 , len(array)):
                dict[array[i]]=array2[i]
            list.append(dict)
    return list

def readQuestionFile(fileName):
    dict ={}
    with open("Guess_Who/{0}".format(fileName)) as file:
        for line in file.readlines():
            array = line.strip().split(" = ")
            dict[array[0]]= array[1]
    return dict

def findGuess(dict):
    list = readFile()
    filterArr=[]
    for el in list :
        isGuess=True
        for key ,value in dict.items():
            if el[key]!= value:
                isGuess = False
                break
        if isGuess :
            filterArr.append(el)
    return filterArr

def main():
    dict1 = readQuestionFile("question1.txt")
    dict2 = readQuestionFile("question2.txt")
    
    print("Question 1")
    for el in findGuess(dict1):
        print("{0} - Gender: {1}, Hair Color: {2}, Hair Length: {3}".format(el["Name"],el["Gender"],el["Hair Color"],el["Hair Length"] ))
    
    print("Question 2")
    for el in findGuess(dict2):
        print("{0} - Gender: {1}, Hair Color: {2}, Hair Length: {3}".format(el["Name"],el["Gender"],el["Hair Color"],el["Hair Length"] ))

if __name__== "__main__" :
    main()

