#%%
from math import floor as mf
from collections import deque
from msilib.schema import Error
from operator import xor
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

    #not being used for now
    def pad_messageSchedule(message_schedule):
        for i in range(16,64):
            message_schedule.append('0'.zfill(32))
        return message_schedule

    # def combine_string_appendBigEndian(self,before_string,lenOfOriginalString):
    #     #pad 0s till theres space for the big endian binary number and append big endian
    #     before_string = ''.join(before_string)
    #     pad_till = self.decimalToBinary(lenOfOriginalString)
    #     print(pad_till)
    #     for i in range(len(before_string), len(before_string)+(64-len(pad_till))):
    #         before_string = before_string + '0'
    #     before_string = before_string + pad_till
    #     return(before_string)

    
    def combine_string_appendBigEndian(self,before_string,lenOfOriginalString):
        #pad 0s till theres space for the big endian binary number and append big endian
        before_string = ''.join(before_string)
        pad_till = self.decimalToBinary(lenOfOriginalString*8)
        
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
        
    def leftRotate(self, messageString, rotateBy= -1):
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
        try:
            a = int(self.rightRotate(x,2),2)
            b = int(self.rightRotate(x,13),2)
            c = int(self.rightRotate(x,22),2)
            result = a^b^c
            result = format(result,'032b')
            return result
        except TypeError:
            a = int(self.rightRotate(self.format(x),2),2)
            b = int(self.rightRotate(self.format(x),13),2)
            c = int(self.rightRotate(self.format(x),22),2)
            result = a^b^c
            result = format(result,'032b')
            return result

    def usigma1(self,x):
        try:
            a = int(self.rightRotate(x,6),2)
            b = int(self.rightRotate(x,11),2)
            c = int(self.rightRotate(x,25),2)
            result = a^b^c
            result = format(result,'032b')
            return result
        except TypeError:
            a = int(self.rightRotate(self.format(x),6),2)
            b = int(self.rightRotate(self.format(x),11),2)
            c = int(self.rightRotate(self.format(x),25),2)
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

    
    def addSigmaProcessing(self,new_message):
        for i in range(16,64):
            w = new_message
            #s0 = self.rightRotate(int(w[i-15],2),7) ^ self.rightRotate(int(w[i-15],2),18) ^ self.shiftRight(int(w[i-15],2),3)
            s0 = self.sigma0(w[i-15])
            #s1 = self.rightRotate(int(w[i-2]),17) ^ self.rightRotate(int(w[i-2]),19) ^ self.shiftRight(int(w[i-2]),10)
            s1 = self.sigma1(w[i-2])
            #w[i] = self.add(w[i-16], s0 , w[i-7] , s1)
            w.append(self.add(w[i-16], s0 , w[i-7] , s1))
            #print(self.add(w[i-16], s0 , w[i-7] , s1))
        return w

    def HexToBinary(self, hexString, num_of_bits=32):
        #returns 32 bit binary number of hex
        hexs = []
        for i in range(len(hexString)):
            hexs.append(bin(int(hexString[i], 16))[2:].zfill(num_of_bits))
        return hexs

    def choice(self,e,f,g):
        try:
            e = int(e,2)
            f = int(f,2)
            g = int(g,2)
            ch = (e & f) ^ ((~e) & g)
            return ch
        except TypeError:
            ch = (e & f) ^ ((~e) & g)
            return ch

    def majority(self,a,b,c):
        try:
            a = int(a,2)
            b = int(b,2)
            c = int(c,2)
            maj = (a & b) ^ (a & c) ^ (b & c)
            return maj
        except TypeError:
            maj = (a & b) ^ (a & c) ^ (b & c)
            return maj

    def compress(self, hashValuesInBinary,constants64_inBinary, message_schedule_with_sigma):     
        # a = '01101010000010011110011001100111' = 0
        # b = '10111011011001111010111010000101' = 1
        # c = '00111100011011101111001101110010' = 2
        # d = '10100101010011111111010100111010' = 3
        # e = '01010001000011100101001001111111' = 4
        # f = '10011011000001010110100010001100' = 5
        # g = '00011111100000111101100110101011' = 6 
        # h = '01011011111000001100110100011001' = 7
        a = hashValuesInBinary[0]
        b = hashValuesInBinary[1]
        c = hashValuesInBinary[2]
        d = hashValuesInBinary[3]
        e = hashValuesInBinary[4]
        f = hashValuesInBinary[5]
        g = hashValuesInBinary[6]
        h = hashValuesInBinary[7]

        A = int(a,2)
        B = int(b,2)
        C = int(c,2)
        D = int(d,2)
        E = int(e,2)
        F = int(f,2)
        G = int(g,2)
        H = int(h,2)
        for i in range(64):
            S1 = int(self.usigma1(E),2)
            ch = self.choice(E,F,G)  
            k = int(constants64_inBinary[i],2)
            w = int(message_schedule_with_sigma[i],2)
            temp1 = H + S1 + ch + k + w

            S0 = int(self.usigma0(A),2)
            maj = self.majority(A,B,C)
            temp2 = S0 + maj
            
            #print(self.format(temp1+temp2))     
            #new  = temp1 + temp2
            # h = g
            # g = f
            # f = e
            # e = self.format((int(d,2) + temp1))
            # d = c
            # c = b
            # b = a
            # a = self.format(new)
            
            H = G
            G = F
            F = E
            E = D + temp1
            D = C
            C = B
            B = A
            A = temp1 + temp2


            # print("i: ",i)
            # print(self.format(A))
            # print(self.format(B))
            # print(self.format(C))
            # print(self.format(D))
            # print(self.format(E))
            # print(self.format(F))
            # print(self.format(G))
            # print(self.format(H))
            # print("\n")
            # inth = intg
            # intg = intf
            # intf = inte
            # inte = intd + temp1
            # intd = intc
            # intc = intb
            # intb = inta
            # inta = temp1 + temp2
              
        #compression_list = [a,b,c,d,e,f,g,h]
        compression_list_inInt = [A,B,C,D,E,F,G,H]
        
        #compressed_with_added_initialValues = self.addInitialHashValues(compression_list_inInt, hashValuesInBinary)
        return self.addInitialHashValues(compression_list_inInt, hashValuesInBinary)
        

    def addInitialHashValues(self, compression_list, hashValuesInBinary):
        a = int(hashValuesInBinary[0],2)
        b = int(hashValuesInBinary[1],2)
        c = int(hashValuesInBinary[2],2)
        d = int(hashValuesInBinary[3],2)
        e = int(hashValuesInBinary[4],2)
        f = int(hashValuesInBinary[5],2)
        g = int(hashValuesInBinary[6],2)
        h = int(hashValuesInBinary[7],2)

        A = compression_list[0]
        B = compression_list[1]
        C = compression_list[2]
        D = compression_list[3]
        E = compression_list[4]
        F = compression_list[5]
        G = compression_list[6]
        H = compression_list[7]

        newA = A + a
        newB = B + b
        newC = C + c
        newD = D + d
        newE = E + e
        newF = F + f
        newG = G + g
        newH = H + h
        
        compression_list = [newA , newB , newC , newD , newE , newF , newG , newH]
        for i in range(len(compression_list)):
            compression_list[i] = self.format(compression_list[i])

        return compression_list


    def format(self,integer):
        return format(integer%2**32,'032b')

    
    def convertAppendHash(self,digest):
        hash = ""
        for i in range(len(digest)):
            hash = hash + hex(int(digest[i],2))[2:]

        print(hash)
        return hash

class FetchRandomText:
    def fetchRandomText(self, URL = "https://baconipsum.com/api/?type=meat-and-filler&paras=5&format=text"):

        response = requests.get(URL)
        if response.status_code == 200:
            print("STATUS: OK")
            return response.text
        else:
            "STATUS: NOT FOUND"
            return None


class Hash:
    def genHash(self,message_schedule_with_sigmaWords,binary_of_hexValues):
        print()



# %%
