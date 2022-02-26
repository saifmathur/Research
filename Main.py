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
#FinalBinary, lengthOfOriginal, Original = preprocessing.S2B("hello world")
FinalBinary, lengthOfOriginal, Original = preprocessing.S2B(fetch.fetchRandomText())



#pad with 0 till string is a multiple of 512
padded = preprocessing.pad(FinalBinary,512)
#print(padded)

#subtract 64 bits for "big-endian"
before_big_endian = preprocessing.processForBigEndian(padded) #448
#print(before_big_endian)

#combine string and add big endian
combined_string_with_bigEndian = preprocessing.combine_string_appendBigEndian(before_big_endian,lengthOfOriginal)
print(combined_string_with_bigEndian)

print("CHECK for multiple of 512:")
print("OK" if len(combined_string_with_bigEndian)%512==0 else "FAILED")


# combined_string = preprocessing.combine_string(before_big_endian)

# #now pad 0s till theres space for the big endian binary number
# #print(len(combined_string))
# #print(len(gc.decimalToBinary(lengthOfOriginal)))
# pad_till = gc.decimalToBinary(lengthOfOriginal)
# for i in range(len(combined_string), len(combined_string)+(64-len(pad_till))):
#     combined_string = combined_string + '0'
# combined_string = combined_string + pad_till

# #print(len(combined_string))
# print(combined_string)




# %%
