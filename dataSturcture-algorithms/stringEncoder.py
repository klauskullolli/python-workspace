"""
This string encoder is used to encode to bits a string in a way that number of bits is less 
and the best optimal way for bits size (not using standard ASCII characters)
This is a technic that follow the most optimal way to merge to arrays (first those with less element)
Same logic is used to form a encoding table according to repetation elements of string 
"""

def calRepetation(word: str) -> dict:
    wordDict = {}
    for e in word:
        if (e not in wordDict):
            wordDict[e] = 1
        else:
            wordDict[e] = wordDict[e] + 1

    return wordDict


def sortDict(dictionary: dict) -> dict:
    return {k: v for k, v in sorted(dictionary.items(), key=lambda x: x[1])}


def createMergeOrder(wordDict: dict):
    mapOrder = {}

    temp = [[k, v] for k, v in wordDict.items()]
    while len(temp) > 1:
        first = temp[0]
        second = temp[1]
        k = first[0] + second[0]
        v = first[1] + second[1]
        del temp[0]
        del temp[0]
        temp.insert(0, [k, v])
        temp = [x for x in sorted(temp, key=lambda x: x[1])]
        if(k not in mapOrder):
            mapOrder[k] = [first[0], second[0]]
    
    return mapOrder


def generateEncodingTable(word: str):
    wordDict = calRepetation(string)
    wordDict = sortDict(wordDict)
    mapOrder =  createMergeOrder(wordDict)
    table = {}
    current =  list(mapOrder.keys())[-1]
    ecodedTable("", current, mapOrder, table)
    return table
    
def ecodedTable(bits: str, char: str, mapOrder: dict , table: dict):
    if(char not in mapOrder):
        table[char] = bits 
        return
    else:
        current = mapOrder[char]
        for i in range(0, len(current)):
            ecodedTable(bits+str(i),current[i], mapOrder, table)  


def encodeString(word:str , table: dict):
    encStr = ""
    for e in word:
        encStr += table[e] 
    return encStr

def decodeString(wordBits: str, table: dict):
    decWord = ""
    revTable = {v:k for k,v in table.items()}
    i = 0 
    j = 1
    length =  len(wordBits)
    while (True):
        if(i>length or j > length):
            break
        bits =  wordBits[i:j]
        
        if (bits in revTable):
            decWord +=revTable[bits]
            i = j 
            j +=1
        else:
            j+=1    
    
    return decWord
        

if __name__ == '__main__':

    string = "ABADDEACCEBBABDEDCACC"

    table = generateEncodingTable(string)
    
    encStr = encodeString(string, table)
    
    decStr = decodeString(encStr, table)
    print(encStr)
    print(decStr)
    print(decStr==string)
