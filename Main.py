#%%
from Tools import GenerateConstants, PreProcessing, FetchRandomText
import requests
gc = GenerateConstants()
preprocessing = PreProcessing()
fetch = FetchRandomText()
list = gc.genCubeRoots(gc.generate(8))
list2 = gc.generate(8)



print(list)

# for i in range(0,len(list2)):
#     print(i," || ",list2[i] , "|| Cube = " ,list2[i]**(1./3.), "|| digits = ",list[i]," || binary of decimal values = ", format(int(list2[i]* 10**16),"b") )


#converting string to binary
FinalBinary, lengthOfOriginal, Original = preprocessing.S2B("abcd")
#FinalBinary, lengthOfOriginal, Original = preprocessing.S2B(fetch.fetchRandomText())



#pad with 0 till string is a multiple of 512
padded = preprocessing.pad(FinalBinary,512)
#print(padded)

#subtract 64 bits for "big-endian"
before_big_endian = preprocessing.processForBigEndian(padded) #448
#print(before_big_endian)

#combine string and add big endian
combined_string_with_bigEndian = preprocessing.combine_string_appendBigEndian(before_big_endian,lengthOfOriginal)
#print(combined_string_with_bigEndian)

print("CHECK for multiple of 512: ")
print("OK" if len(combined_string_with_bigEndian)%512==0 else "FAILED")


#break into 512 bit chunks
print("breaking message into 512 bit chunks...")
message_chunked_to_512 = preprocessing.break_into_512_chunks(combined_string_with_bigEndian)


#print chunks
#preprocessing.printChunked(message_chunked_to_512)


#gen hashed constants
gc.genHashedConstants()

# %%
