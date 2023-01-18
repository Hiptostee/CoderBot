import pandas as pd

norm = ["q", "w", "e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",' ',"_", "1", "2",'3','4','5','6','7','8','9']
coder = ['w','e','d','t','y','h','j','k','l','q','z','i','f','g','o','p','r','s','a','x','c','v','b','n','m','u', "_", ' ', '1', '6', '11', '16','21', "26", '29', '36', '41']

def codify(stringie):
    stringlist = []
    finallist = []
    for i in stringie:
        stringlist.append(i)
    for i in stringlist:
        if i not in norm:
            finallist.append(i)
        else:
            finallist.append(coder[norm.index(i)])
    return(''.join(finallist))

def decodify(codeie):
    codelist = []
    finallist = []
    for i in codeie:
        codelist.append(i)
    for i in codelist:
        if i not in coder:
            finallist.append(i)
        else:
            finallist.append(norm[coder.index(i)])
    return(''.join(finallist))

def table():
    print("-" * 17)
    print(pd.DataFrame(list(zip(norm, coder)),columns =['Original', 'Coded']))
    print("-" * 17)
