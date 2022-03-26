from Tools import PreProcessing
pre = PreProcessing()

class ModSHA:
    def addSigmaProcessingWithMod(self, new_message):
        for i in range(16,64):
            w = new_message
            s0 = MathFunctions.sigma0Mod(w[i-15])
            s1 = MathFunctions.sigma1Mod(w[i-2])
            w.append(pre.add(w[i-16],s0,w[i-7],s1))
        return w

class MathFunctions:
    def sigma0Mod(self,x):
        #print()
        a = int(pre.leftRotate(x,rotateBy = -7),2)
        b = int(pre.leftRotate(x,rotateBy = -18),2)
        c = int(pre.shiftLeft(x,3),2)
        result = a^b^c^c
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
        print()

    def usigma1Mod(self,x):
        print()

    def choice(self,e,f,g):
        print()

    def majority(self,a,b,c):
        print()


class GenModHash:
    def GenModHash(self):
        print()