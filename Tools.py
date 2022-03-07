#%%
from math import floor as mf
from collections import deque
from msilib.schema import Error
from unittest import result #to right rotate
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
    
    def genSquareRoots(self,primeList):
        squareRootList = []
        for i in range(len(primeList)):
            square = math.sqrt(primeList[i])
            fractional = square - math.floor(square)
            squareRootList.append(fractional)
        return squareRootList

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


    def hashValues(self, value=8):
        cubeList = self.genSquareRoots(self.generate(value))
        hash_values = self.calHexOfCube(cubeList=cubeList,hexForm=True)
        return hash_values


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
           
    def createMessageSchedule(self, chunkList, n=32):
        #message_schedule = [chunkList[i:i+n] for i in range(0, len(chunkList), n)]
        message_schedule = []
        for i in range(len(chunkList)):
            for j in range(0,len(chunkList[i]),n):
                message = chunkList[i][j:j+n]
                message_schedule.append(message)
        return message_schedule

    def rightRotate(self, messageString, rotateBy = 1):
        #rotatedMessage = []
        if not rotateBy < 0:
            items = deque(messageString)
            items.rotate(rotateBy)
            return ''.join(items) 
        else:
            raise Error("'Rotateby' should be positive")
        
    def leftRotate(self, messageString, rotateBy=-abs(1)):
        if rotateBy < 0:
            items = deque(messageString)
            items.rotate(rotateBy)
            return ''.join(items) 
        else:
            raise Error("'Rotateby' should be negative")

    
    

    def shiftRight(self, messageString, shiftBy = 1):
        if shiftBy < 32: 
            messageString = int(messageString,2)
            result = messageString >> shiftBy
            #print(result)
            result = format(result,'032b')
            return result
        else:
            raise Error("'shiftBy' factor cannot be negative" + str(shiftBy))

    def shiftLeft(self, messageString, shiftBy = 1):
        if shiftBy < 32:
            shiftBy = shiftBy-1
            messageString = int(messageString,2)
            result = messageString << shiftBy
            #print(result)
            result = format(result,'032b')
            return str(result)[shiftBy:]
        else:
            raise Error("Change 'shiftBy' factor")


    def sigma0(self,x):
        a = int(self.rightRotate(x,7),2)
        b = int(self.rightRotate(x,18),2)
        c = int(self.shiftRight(x,3),2)
        result = a^b^c
        result = format(result,'032b')
        return result

    def sigma1(self,x):
        a = int(self.rightRotate(x,17),2)
        b = int(self.rightRotate(x,19),2)
        c = int(self.shiftRight(x,10),2)
        result = a^b^c
        result = format(result,'032b')
        return result

    def usigma0(self,x):
        a = int(self.rightRotate(x,2),2)
        b = int(self.rightRotate(x,13),2)
        c = int(self.rightRotate(x,22),2)
        result = a^b^c
        result = format(result,'032b')
        return result

    def usigma1(self,x):
        a = int(self.rightRotate(x,6),2)
        b = int(self.rightRotate(x,11),2)
        c = int(self.rightRotate(x,25),2)
        result = a^b^c
        result = format(result,'032b')
        return result

    def add(self, w1,s0,s1,w2):
        #w0 = int(w1,2)
        #s0 = int(s0,2)
        #w2 = int(w2,2)
        #s1 = int(s1,2)
        result = int(w1,2) + int(s0,2) + int(w2,2) + int(s1,2)
        result = format(result%2**32,'032b')
        return result

    # def refineMessageSchedule(self, message_schedule):
    #     #calculates remaining 48 words
    #     for i in range(16,63):
    #         toAppend = 
    #         message_schedule.append(message_schedule[i-2])
       

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






# %%
