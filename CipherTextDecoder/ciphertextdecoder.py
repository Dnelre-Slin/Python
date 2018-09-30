# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:54:30 2018

@author: Nils
"""

#class 

def intToLetter(_int):
    _int = _int % (ord("Z") - ord("A") + 1) #Mod to alphabet (Capital letters only)
    return chr(_int + ord("A"))

def letterToInt(letter):
    ord(letter) - ord("A")
    return ord(letter) - ord("A")

def letterIncrement(letter, increment=1):
    return intToLetter(letterToInt(letter) + increment)

def doPrint(cyphertext, keys, plaintexts):
    plaintext = ""
    for i in range(len(cyphertext)):
        plaintext += keys[cyphertext[i]]
    plaintexts += plaintext
    
def findTaken(level, cypherfixed, keys, taken):
 #   print("test:", taken[level:])
    while keys[cypherfixed[level]] in taken[level+1:]:
        keys[cypherfixed[level]] = letterIncrement(keys[cypherfixed[level]])
#        print("hmm")
    return keys[cypherfixed[level]]

def decodeReq(level, cyphertext, cypherfixed, keys, taken, plaintexts):
    first = keys[cypherfixed[level]]
    taken[level] = findTaken(level, cypherfixed, keys, taken)
    
    runLoop = True
    
    while runLoop:
        if (level <= 0):
            doPrint(cyphertext, keys, plaintexts)
        else:
            decodeReq(level-1, cyphertext, cypherfixed, keys, taken, plaintexts)
        
        keys[cypherfixed[level]] = letterIncrement(keys[cypherfixed[level]])
        taken[level] = findTaken(level, cyphertext, keys, taken)
        
        if keys[cypherfixed[level]] == first:
            runLoop = False
        

def decoder(cyphertext):
    keys = {}
    cypherfixed = ""
    taken = []
    plaintexts = []
    for i in range(len(cyphertext)):
        if cyphertext[i] not in keys:
            keys[cyphertext[i]] = cyphertext[i]
            cypherfixed += cyphertext[i]
            taken += cyphertext[i]
    decodeReq(len(keys)-1, cyphertext, cypherfixed, keys, taken, plaintexts)
    return plaintexts

def decoderOld(cyphertext):
    keys = {}
    cypherfixed = ""
    for i in range(len(cyphertext)):
        if cyphertext[i] not in keys:
            keys[cyphertext[i]] = cyphertext[i]
            cypherfixed += cyphertext[i]
            
    plaintext = ""
    
    for i in range(len(keys)):
        for j in range(0, i+1):
            for k in range(0, 26):
                keys[cypherfixed[j]] = letterIncrement(keys[cyphertext[j]])
                plaintext = ""
                for l in range(len(cyphertext)):
                    plaintext += keys[cypherfixed[l]]
                print(plaintext)
    
    

cyphertext = "BT JPX RMLX PCUV AMLX ICVJP IBTWXVR CI M LMT’R PMTN, MTN YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX YMGG CI JPX HBTW’R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX PMTN JPMJ YVCJX. JPXT JPX HBTW’R ACUTJXTMTAX YMR APMTWXN, MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR, JPX APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX, MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI, RPMGG FX AGCJPXN YBJP RAM"

plaintext = ""

keys = {}
#keys["M"] = "a"
#keys["L"] = "c"
#keys["T"] = "n"
#keys["R"] = "t"


#keys["J"] = "t"
#keys["P"] = "h"
#keys["X"] = "e"

#keys["N"] = "d"

#keys["B"] = "i"

for i in range(len(cyphertext)):
    if cyphertext[i] in keys:
        plaintext += keys[cyphertext[i]]
    else:
        plaintext += cyphertext[i]
        
print(plaintext)

#cypherword = "AMTNGXRJBAH"
cypherword = "JPX"
plainwords = []

#while True:
 #   plainwords += ""
    #for i in range(len(cypherword)):
        
print("Start")

plaintexts = decoder(cypherword)

print(plaintexts[100:110])

print("End")