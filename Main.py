#%%
from asyncio import constants
import chunk

from Tools import GenerateConstants, PreProcessing, FetchRandomText
import requests
gc = GenerateConstants()
preprocessing = PreProcessing()
fetch = FetchRandomText()


#converting string to binary
FinalBinary, lengthOfOriginal, Original = preprocessing.S2B("hello world")
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


primeList = gc.generate(64)
cubeList  = gc.genCubeRoots(primeList)
#print(cubeList)
constants64 = gc.calHexOfCube(cubeList)
#print(constants64)


#get hash values
hash_values = gc.hashValues()
#print(hash_values)


#create message schedule
message_schedule = preprocessing.createMessageSchedule(chunkList=message_chunked_to_512)
#print(message_schedule,"\nLenght of message schedule: ",len(message_schedule))


s0 = preprocessing.sigma0('01101111001000000111011101101111')
s1 = preprocessing.sigma1('00000000000000000000000000000000')
#print(s0)
# w1 = int('01101000011001010110110001101100',2) + int('11001110111000011001010111001011',2) + int('00000000000000000000000000000000',2) + int('00000000000000000000000000000000',2)
# print(w1)
# print(format(w1,'032b'))
# print(format(w1%2**32,'032b'))

w1 = preprocessing.add('01101000011001010110110001101100',s0,'00000000000000000000000000000000',s1)
print(w1)
# %%
