#%%
from Tools import GenerateConstants, PreProcessing, FetchRandomText
import requests
gc = GenerateConstants()
preprocessing = PreProcessing()
fetch = FetchRandomText()
list = gc.genCubeRoots(gc.generate(64))
list2 = gc.generate(64)
# for i in range(0,len(list2)):
#     print(i," || ",list2[i] , "|| Cube = " ,list2[i]**(1./3.), "|| digits = ",list[i]," || binary of decimal values = ", format(int(list2[i]* 10**16),"b") )


#converting string to binary
FinalBinary, lengthOfOriginal, Original = preprocessing.S2B("hello world")
print(FinalBinary,"\n",lengthOfOriginal)


print("Length of Original in binary, to be appended to the padded list = ", gc.decimalToBinary(lengthOfOriginal))
#Val = s2b.S2B(fetch.fetchRandomText())


#pad with 0 till string is a multiple of 512
#padded = preprocessing.pad(Val,512)
#print(padded)

#subtract 64 bits for "big-endian"
#print(preprocessing.processForBigEndian(padded))






# %%
