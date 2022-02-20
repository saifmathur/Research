#%%
from Tools import GenerateConstants, StringToBinary, FetchRandomText
import requests
gc = GenerateConstants()
s2b = StringToBinary()
fetch = FetchRandomText()
list = gc.genCubeRoots(gc.generate(64))
list2 = gc.generate(64)
# for i in range(0,len(list2)):
#     print(i," || ",list2[i] , "|| Cube = " ,list2[i]**(1./3.), "|| digits = ",list[i]," || binary of decimal values = ", format(int(list2[i]* 10**16),"b") )



Val = s2b.S2B("hello")
#Val = s2b.S2B(fetch.fetchRandomText())
padded = s2b.pad(Val,512)
print(padded)
#print(Val)





# %%
