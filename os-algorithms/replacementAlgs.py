import copy

def FIFO(frameString: str, frameSize: int ):
    
    pageTack = []
    frames = frameString.split(",")
    page = []
    miss = 0 
    hit = 0 
    
    for frame in frames:
        if frame in page:
            hit +=1
        else:
            miss +=1
            if len(page)==frameSize:
                page.pop(0)
                page.append(frame)
            else:
                page.append(frame)
        pageTack.append(copy.deepcopy(page))        
    
    return pageTack, miss ,hit

def LRU(frameString: str, frameSize: int):
    
    pageTack = []
    frames = frameString.split(",")
    page = []
    miss = 0 
    hit = 0 
    
    for frame in frames:
        if frame in page:
            index = page.index(frame)
            page.pop(index)
            page.insert(0, frame)
            hit +=1
        else:
            miss +=1
            if len(page)==frameSize:
                page.pop()
                page.insert(0, frame)
            else:
                page.insert(0, frame)
        pageTack.append(copy.deepcopy(page))        
    
    return pageTack, miss ,hit

def replacement(page: list, remainFrames: list):
    noIndex = len(remainFrames)
    pageIndex = {}
    for  el in page: 
        if el in remainFrames:
            pageIndex[el] = remainFrames.index(el)
        else:
            return el
    frames = sorted(pageIndex.items() , key = lambda x:x[1])      
    return frames[-1][0]

def OPTIMAL(frameString: str, frameSize: int):
    
    pageTack = []
    frames = frameString.split(",")
    copyFrame = copy.deepcopy(frames)
    page = []
    miss = 0 
    hit = 0 
    
    for frame in frames:
        if frame in page:
            hit +=1
        else:
            miss +=1
            if len(page)==frameSize:
                removeFrame = replacement(page, copyFrame)
                page.remove(removeFrame)
                page.append(frame)
            else:
                page.append(frame)
        copyFrame.remove(frame)
        pageTack.append(copy.deepcopy(page))        
    
    return pageTack, miss ,hit 



def SECOND_CHANCE(frameString: str, frameSize: int):
    
    pageTack = []
    frames = frameString.split(",")
    page = []
    secondChance = []
    miss = 0 
    hit = 0 
    
    for frame in frames:
        if frame in page:
            if frame not in secondChance:
                secondChance.append(frame)
            hit +=1
        else:
            miss +=1
            if len(page)==frameSize:
                
                for i in range(frameSize):
                    if page[i] not in secondChance:
                        popped = page.pop(i)
                        break 
                if(len(page)==frameSize):
                    popped = page.pop(0)
                    
                if popped in secondChance :
                        secondChance.remove(popped)
                        
                page.append(frame)
            else:
                page.append(frame)
        pageTack.append(copy.deepcopy(page))        
    
    return pageTack, miss ,hit

  
if __name__ == "__main__":
    frameString ="A,B,C,F,B,K,D,B,B,C,A,D,A,R,E,G,A,B,F,G"
    frameSize = 4
    pageTack, miss, hit = FIFO(frameString, frameSize)  
    
    print("------------- FIFO ---------------")
    print("Page Track:")
    for pages in pageTack:
        print(pages)

    print(f"Miss: {miss}")
    print(f"Hit: {hit}")
    
    pageTack, miss, hit = LRU(frameString, frameSize)
    
    print("------------- LRU ---------------")
    print("Page Track:")
    for pages in pageTack:
        print(pages)

    print(f"Miss: {miss}")
    print(f"Hit: {hit}")
    
    
    pageTack, miss, hit = OPTIMAL(frameString, frameSize)
    
    print("------------- OPTIMAL ---------------")
    print("Page Track:")
    for pages in pageTack:
        print(pages)

    print(f"Miss: {miss}")
    print(f"Hit: {hit}")
    
    
    pageTack, miss, hit = SECOND_CHANCE(frameString, frameSize)
    
    print("------------- SECOND CHANCE ---------------")
    print("Page Track:")
    for pages in pageTack:
        print(pages)

    print(f"Miss: {miss}")
    print(f"Hit: {hit}")