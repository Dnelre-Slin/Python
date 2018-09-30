# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:17 2018

@author: Nils
"""

def intToLetter(_int, first = "A", last = "Z"):
    _int = _int % (ord(last) - ord(first) + 1) #Mod to alphabet (Capital letters only)
    return chr(_int + ord(first))

def letterToInt(letter, first = "A"):
    ord(letter) - ord(first)
    return ord(letter) - ord(first)

def letterIncrement(letter, increment=1, first = "A", last = "Z"):
    return intToLetter(letterToInt(letter, first) + increment, first, last)

def caesarTest(ciphertext):
#    ciphertext = "vwduw"
    plaintexts = []
    
    for i in range(ord('z') - ord('a')):
        plaintext = ""
        for j in range(len(ciphertext)):
            plaintext += letterIncrement(ciphertext[j], i, "a", "z")
        plaintexts.append(plaintext)
    #    print(plaintext)
    
    for i in range(len(plaintexts)):
        print(plaintexts[i], "(Shift:", i, ")")
    
def caesarShift(text, shift):
    result = ""
    for i in range(len(text)):
        result += letterIncrement(text[i], shift, "a", "z")
    return result

def polycipher(ct, key, offset = 0):
    pt = ""
    for i in range(len(ct)):
        pt += letterIncrement(ct[i], -letterToInt(key[(i + offset) % len(key)], "a"), "a", "z")
    return pt

def multiply2(ct):
    pt = ""
    for i in range(len(ct)):
        pt += letterIncrement(ct[i], letterToInt(ct[i])*2, "a", "z")
    return pt

def poly2mat(a,b,key=""):
    alf = "abcdefghijklmnopqrstuvwxy"
    mat = ""
    
    for i in range(len(key)):
        if key[i] not in mat:
            mat += key[i]
    
    for i in range(len(alf)):
        if alf[i] not in mat:
            mat += alf[i]
    
#    print(mat)
    return mat[b*5+a]
    
        
#    mat = []
#    mat.append(["r","a","i","l","w"])
#    mat.append(["y","v","e","b","c"])
#    mat.append(["d","f","g","h","k"])
#    mat.append(["m","n","o","p","q"])
#    mat.append(["s","t","u","x","z"])
#    
#    return mat[a][b]

#def poly2matOld(a,b):
#    mat = []
#    mat.append(["a","b","c","d","e"])
#    mat.append(["f","g","h","i","k"])
#    mat.append(["l","m","n","o","p"])
#    mat.append(["q","r","s","t","u"])
#    mat.append(["v","w","x","y","z"])
#    
#    return mat[a][b]

def poly2(ct, key = ""):
    pt = ""
    for i in range(0,len(ct),2):
        a = int(ct[i]) - 1
        b = int(ct[i+1]) - 1 
        pt += poly2mat(a,b,key)
    return pt

def matcracker(a,b):
    mat = []
    mat.append(["a","f","k","p","u"])
    mat.append(["b","g","l","_","v"])
    mat.append(["c","h","m","r","_"])
    mat.append(["d","i","n","s","_"])
    mat.append(["e","_","o","t","y"])
    
    return mat[a][b]

def polycracker(ct):
    pt = ""
    for i in range(0,len(ct),2):
        a = int(ct[i]) - 1
        b = int(ct[i+1]) - 1 
        pt += matcracker(a,b)
    return pt
        
#caesarTest("vwduw")
    
ct1 = ""

ct1 += "gluntlishjrvbadvyyplkaoh"
ct1 += "avbyjpwolypzavvdlhrvuu"
ct1 += "leatlzzhnlzdpajoavcpnl"
ct1 += "ulyljpwolyrlfdvykpzaolo"
ct1 += "pkkluzftivsvmklhaoput"
ct1 += "fmhcvypalovsilpuluk"

ct2 = ""
        
ct2 += "vwduwljudeeghgyhybwklq"
ct2 += "jlfrxogilqgsohdvhuhwxuq"
ct2 += "dqbeoxhsulgwviruydxowd"
ct2 += "qgdodupghvljqedvhgrqzk"
ct2 += "lfkedqnbrxghflghrqldpvhw"
ct2 += "wlqjxsvdihkrxvhfr"

pt = caesarShift(ct1, 19) + "\n\n" + caesarShift(ct2, 23)

#caesarTest(ct2)
#print(caesarShift(ct6, 19))

#print(pt)

ct3 = "klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"
key1 = "sskkuullll"
#key1 = "skull"

ctt = "xzetgstvaxivgighicntyaivcscibq"
keyy = "crypto"

pt3 = polycipher(ct3, key1)
#pt3 = multiply2(pt3)

#print(pt3)

#for i in range(1):
#    print(polycipher(ct3, key1, i), end="\n\n")

#  nerailwyvubcdfghkmopqstxz
#  nerailwyvubcdfghkmopqstxz

ct4 = "4454113454112333534454124243424432514121231131135315544254424442434432514153435432423441112551355334134243225343114454345343225134314214325134125334121554153451335144441122514442544244441534512355154321345111131121235142543153332142435144531534143451254253154433515432534144"
ct5 = "43513544"

ctt2 = "4423244324431143151342154432154343112215"

ctB = "114454345343225134314214325134125334121554153451"
ctE = "335144441122514442544244441534512355154321345111131121235142543153332142435144531534143451254253154433515432534144"

ctF = ct4[194:]
print(ctF)

#print(poly2(ct4,"nerailwyvu"))
#print(poly2(ct5))

print(poly2(ct5))