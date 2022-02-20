#%%
import requests

class GenerateConstants:
    constList = []
    def isPrime(self, n):
        if n==1 or n==0:
            return False
        for i in range(2,n):
            #if the number is divisible by i then not a prime
            if(n%i==0):
                return False
        return True


    def generate(self, length):
        i = 0
        while len(self.constList) != length:
            if self.isPrime(i):
                self.constList.append(i)
            i = i+1
        
        return self.constList     
        
    def genCubeRoots(self,List):
        cubeList = []
        for i in range(len(List)):
            #print(List[i])
            #print("cube =" , List[i]**(1./3.))
            digits = len(str(List[i] **(1./3.)))
            digits = digits - 2
            #print(digits)
            cubeList.append(digits)
        return cubeList    
            #cubeList.append()


    def toBinary(self, num):
        if num >=1:
            self.toBinary(num // 2)
        print(num%2,end='')


class StringToBinary:
    def S2B(self, string):
        res = []
        for i in string:
            #print(bin(ord(i))[2:].zfill(8)) #to eliminate 0b
            #zfill() 0 pad to make it of len 8
            res.append(bin(ord(i))[2:].zfill(8))
        
        res.append(str(1).ljust(8,'0'))
        return res

    def pad(self, list ,multiple):
        while not (len(list)/multiple*8).is_integer():
            list.append('0'.zfill(8))
            #subtract 64 bits from the end continue
        print("length of list given is now = ", len(list))
        print("length of data bits in the list is now = ", len(list*8))
        return list
            
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


