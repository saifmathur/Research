from Tools import PreProcessing
pre = PreProcessing()
from Preprocessing import Preprocessing
class MathFunctions:
    def sigma0Mod(self,x):
        a = int(pre.leftRotate(x,rotateBy = -7),2)
        b = int(pre.leftRotate(x,rotateBy = -18),2)
        c = int(pre.shiftLeft(x,3),2)
        result = a^b^c
        result = format(result,'032b')
        return result
  
    def sigma1Mod(self,x):
        #print()
        a = int(pre.leftRotate(x,-17),2)
        b = int(pre.leftRotate(x,-19),2)
        c = int(pre.leftRotate(x,-10),2)
        result = a^b^c
        result = format(result,'032b')
        return result

    def usigma0Mod(self,x):
        try:
            a = int(pre.leftRotate(x,-2),2)
            b = int(pre.leftRotate(x,-13),2)
            c = int(pre.leftRotate(x,-22),2)
            result = a^b^c
            result = format(result,'032b')
            return result
        except TypeError:
            a = int(pre.leftRotate(pre.format(x),-2),2)
            b = int(pre.leftRotate(pre.format(x),-13),2)
            c = int(pre.leftRotate(pre.format(x),-22),2)
            result = a^b^c
            result = format(result,'032b')
            return result

    def usigma1Mod(self,x):
        try:
            a = int(pre.leftRotate(x,-6),2)
            b = int(pre.leftRotate(x,-11),2)
            c = int(pre.leftRotate(x,-25),2)
            result = a^b^c
            result = format(result,'032b')
            return result
        except TypeError:
            a = int(pre.leftRotate(pre.format(x),-6),2)
            b = int(pre.leftRotate(pre.format(x),-11),2)
            c = int(pre.leftRotate(pre.format(x),-25),2)
            result = a^b^c
            result = format(result,'032b')
            return result

    def choice(self,a,c,e): #taking A,C,E
        #changes to logical operation
        #OR
        try: 
            a = int(a,2)
            c = int(c,2)
            e = int(e,2)
            ch = (a|c) ^ ((~a)|e)
            return ch
        except TypeError:
            ch = (a|c) ^ ((~a)|e)
            return ch

    def majority(self,b,d,h): 
        #changes to logical operation and constants
        try:
            b = int(b,2)
            d = int(d,2)
            h = int(h,2)
            maj = (b|d) ^ (b|h) ^ (d|h)
            return maj
        except TypeError:
            maj = (b|d) ^ (b|h) ^ (d|h)
            return maj




class Mod2SHA:
    mf = MathFunctions()
    def addSigmaProcessingWithMod(self, new_message):
        for i in range(16,64):
            w = new_message
            s0 = self.mf.sigma0Mod(x=w[i-15])
            s1 = self.mf.sigma1Mod(x=w[i-2])
            w.append(pre.add(w[i-16],s0,w[i-7],s1))
        return w
    
    def ModCompression(self,hashValuesInBinary,constants64_inBinary, message_schedule_with_ModSigma):
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
            S1 = int(self.mf.usigma1Mod(E),2)
            #ch = pre.choice(E,F,G)
            ch = self.mf.choice(A,C,E)  
            k = int(constants64_inBinary[i],2)
            w = int(message_schedule_with_ModSigma[i],2)
            temp1 = H + S1 + ch + k + w

            S0 = int(self.mf.usigma0Mod(A),2)
            #maj = pre.majority(A,B,C)
            maj = self.mf.majority(B,D,H)
            temp2 = S0 + maj

            H = G
            G = F
            F = E
            E = D + temp1
            D = C
            C = B
            B = A
            A = temp1 + temp2
        
        compression_list_inInt = [A,B,C,D,E,F,G,H]
        return pre.addInitialHashValues(compression_list_inInt, hashValuesInBinary)
        

class GenModHash:
    preprocessing = PreProcessing()
    mod = Mod2SHA()
    message_schedule, hash_values, constants64_binary = Preprocessing().preprocess()
    binary_of_hexValues = preprocessing.HexToBinary(hash_values)
    def genMod2Hash(self):
        message_schedule_with_sigmaWordsMOD = self.mod.addSigmaProcessingWithMod(self.message_schedule)
        digest = self.mod.ModCompression(self.binary_of_hexValues,self.constants64_binary,message_schedule_with_sigmaWordsMOD)
        self.preprocessing.convertAppendHash(digest)