#Problem 2
#Peter D.


def plural():
    word = input("Give me a word ")
    
    if word.endswith("s")or word.endswith("sh")or word.endswith("x")or word.endswith("ch")or word.endswith("z"):
        print( word[0: ] + "es")
    elif word.endswith("ay")or word.endswith("ey")or word.endswith("iy")or word.endswith("oy")or word.endswith("uy"):
        print( word[0: ] + "s")
    elif word.endswith("y"):
        print( word[0:-1] + "ies")
    elif word.endswith("ao")or word.endswith("eo")or word.endswith("io")or word.endswith("oo")or word.endswith("uo"):
        print( word[0: ] + "s")
    elif word.endswith("o"):
        print( word[0: ] + "es")
    elif word.endswith("fe"):
        print( word[0:-2] + "ves")
    elif word.endswith("f"):
        print( word[0:-1] + "ves")
    else:
        print( word[0: ] + "s")
    
if __name__ == "__main__":    
    plural()