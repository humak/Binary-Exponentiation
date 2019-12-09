#udl computational tools for problem solving lab6
#humakal
#'19
import math

def repInBinary(e): 
    eBin = []
    while(e != 0 ):
        eBin.append(e%2)
        e = int(e/2)
    eBin.reverse()
    return eBin
        

def binaryExponentiation(b, e, n):
    #b^e (modn)
    eBin = repInBinary(e)
    mult = 1    
    for i in range (1, len(eBin)):
        mult *= (b**(2**i))** eBin[i]
        mult = mult % n
    return mult

def main():
    print(binaryExponentiation(5,10,18))
    

if __name__== "__main__":
  main()

