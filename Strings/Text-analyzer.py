#Problem 4
#Author: Dewar P.

from string import ascii_letters

def analyze():
    o = open("gettysburg.txt")
    l = ""
    unique_words = []
    unique_count = 0
    stop_count = 0
    
    for x in o:
       l = l + x
       
    allwords = l.split()
    
    i = 0 
    
    while i < len(allwords):
        allwords[i] = allwords[i].lower()
        if allwords[i] == "--":
            allwords[i] = allwords.remove("--")
        elif allwords[i][-1] not in ascii_letters:
            allwords[i] = allwords[i][0:-1]
            
            
        i = i +1
        
    i = 1
    
    print("The total numbers of words in the text:", len(allwords))
    
    while i < len(allwords):
        if allwords[i]not in allwords[i+1:-1]:
            unique_count = unique_count + 1
            unique_words.append(allwords[i])
        i = i+1
        
    unique_words.sort(key=str)
    print("The number of unique words: ", unique_count-1)
    print("The unique words in alphabetical order:")
    i = 1
    # print("The unique words in alphabetical order:",unique_words[1:])
    while i < unique_count:
        print(i, unique_words[i])
        i+=1
    
    i = 1
    
    while i < len(unique_words):
        if "the" == unique_words[i]:
            stop_count = stop_count + 1
        elif "is" == unique_words[i]:
            stop_count = stop_count + 1
        elif "at" == unique_words[i]:
            stop_count = stop_count + 1
        elif "which" == unique_words[i]:
            stop_count = stop_count + 1
        elif "on" == unique_words[i]:
            stop_count = stop_count + 1
        i = i+1
    
    i = 0
    v = 0
        
    print("The amount of stop/unique words are:", stop_count)
    
    for q in unique_words:
        i = i + len(str(q))
        
    for k in allwords:
        v = v + len(str(k))
        
    d = v//len(allwords)
        
    h = i//len(unique_words)
    
    print("The average legnth of unique words:", h)
    print("The average legnth of words:", d)
        
analyze()