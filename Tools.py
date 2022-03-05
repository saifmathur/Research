#%%
from math import floor as mf
import requests
import math
class GenerateConstants:
    
    def isPrime(self, n):
        if n==1 or n==0:
            return False
        for i in range(2,n):
            #if the number is divisible by i then not a prime
            if(n%i==0):
                return False
        return True


    def generate(self, length):
        constList = []
        i=0
        while not len(constList) == length:
            if self.isPrime(i):
                constList.append(i)
            i=i+1
        
        return constList
        
        
        
    def genCubeRoots(self,primeList):
        cubeList = []
        for i in range(len(primeList)):
            root = primeList[i] **(1/3.0)
            #fractional part
            fractional = root - math.floor(root)
            cubeList.append(fractional)
        return cubeList

    def calHexOfCube(self,cubeList,hexForm = True):
        constants = []
        for i in range(len(cubeList)):
            hexString = ""
            fractional = cubeList[i]
            #num = cubeList[i]*16
            #intPart = mf(num)
            #fractPart = num - intPart
            for j in range(8):
                product = fractional * 16
                carry = mf(product)
                fractional = product - mf(product)
                if carry > 9:
                    hexString = hexString + hex(carry).removeprefix("0x")
                else:
                    hexString = hexString + str(carry)

            #print(hexString)
            hexString = "0x" + hexString
            constants.append(hexString)
        print("Constants generated. \n Length of constants list: " , len(constants))
        #print(constants,"length: ",len(constants))
        if hexForm:
            return constants    
        else:
            hexToBinary = []
            for i in range(len(constants)):
                hexToBinary.append(bin(int(constants[i], 16))[2:].zfill(32))
            return hexToBinary    

            

    def toBinary(self, num):
        if num >=1:
            self.toBinary(num // 2)
        print(num%2,end='')

    def decimalToBinary(self,n):
        str1 = bin(n).replace("0b", "0")
        #return str1.ljust(8,'0')
        return str1

class PreProcessing:
    def S2B(self, string):
        res = []
        originalStringBits = []
        originalStringLength = 0
        for i in string:
            #print(bin(ord(i))[2:].zfill(8)) #to eliminate 0b
            #zfill() 0 pad to make it of len 8
            res.append(bin(ord(i))[2:].zfill(8))
        originalStringLength = len(res)
        originalStringBits = res
        res.append(str(1).ljust(8,'0'))
        return res, originalStringLength, originalStringBits

    def pad(self, list ,multiple):
        while not (len(list)/multiple*8).is_integer():
            list.append('0'.zfill(8))
            #subtract 64 bits from the end continue
        print("length of list given is now = ", len(list))
        print("length of data bits in the list is now = ", len(list*8))
        return list
    
    def processForBigEndian(self, padded_list):
        length = len(padded_list)
        del padded_list[length-8:length]
        #print(padded_list)
        #print("data length: ",len(padded_list)*8)
        padded_list_with_bigEndian_space = padded_list
        return padded_list_with_bigEndian_space

    def add_bigEndianNumber(self, length):
        length_to_binary = bin(length).replace('0b','0')
        print(length_to_binary)  
        return length_to_binary

    def decimalToBinary(self,n):
        str1 = bin(n).replace("0b", "0")
        #return str1.ljust(8,'0')
        return str1
    
    def combine_string_appendBigEndian(self,before_string,lenOfOriginalString):
        #pad 0s till theres space for the big endian binary number and append big endian
        before_string = ''.join(before_string)
        pad_till = self.decimalToBinary(lenOfOriginalString)
        for i in range(len(before_string), len(before_string)+(64-len(pad_till))):
            before_string = before_string + '0'
        before_string = before_string + pad_till
        return(before_string)

    def break_into_512_chunks(self, str):
        n = 512
        chunks = [str[i:i+n] for i in range(0, len(str), n)]
        #print(chunks)
        return chunks
        
    def printChunked(self, list):
        print("Number of chunks = ",len(list))
        for i in range(len(list)):
            print("------------")
            print("Block ", i ,"\n" , list[i] + "\n")
           
    
class FetchRandomText:
    def fetchRandomText(self, URL = "https://baconipsum.com/api/?type=meat-and-filler&paras=5&format=text"):

        response = requests.get(URL)
        if response.status_code == 200:
            print("STATUS: OK")
            return response.text
        else:
            "STATUS: NOT FOUND"
            return None

class PreparePadding:
    def prepPad(self, list):
        print()




