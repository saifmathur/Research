#%%

from Tools import GenerateConstants, PreProcessing, FetchRandomText
import requests
gc = GenerateConstants()
preprocessing = PreProcessing()
fetch = FetchRandomText()


#converting string to binary
#FinalBinary, lengthOfOriginal, Original = preprocessing.S2B("hello world")
FinalBinary, lengthOfOriginal, Original = preprocessing.S2B("")
#FinalBinary, lengthOfOriginal, Original = preprocessing.S2B(fetch.fetchRandomText())


#pad with 0 till string is a multiple of 512
padded = preprocessing.pad(FinalBinary,512)
#print(padded)

#subtract 64 bits for "big-endian"
before_big_endian = preprocessing.processForBigEndian(padded) #448
#print(len(before_big_endian), lengthOfOriginal)


#combine string and add big endian
combined_string_with_bigEndian = preprocessing.combine_string_appendBigEndian(before_big_endian,lengthOfOriginal)



print("CHECK for multiple of 512: ")
print("OK" if len(combined_string_with_bigEndian)%512==0 else "FAILED")


#break into 512 bit chunks
print("breaking into 512 bit chunks...")
message_chunked_to_512 = preprocessing.break_into_512_chunks(combined_string_with_bigEndian)


#print chunks
#preprocessing.printChunked(message_chunked_to_512)


primeList = gc.generate(64)
cubeList  = gc.genCubeRoots(primeList)
#print(cubeList)
constants64 = gc.calHexOfCube(cubeList)
#print(constants64)
constants64_binary = preprocessing.HexToBinary(constants64)

#get hash values
hash_values = gc.hashValues()
#print(hash_values)


#create message schedule
message_schedule = preprocessing.createMessageSchedule(chunkList=message_chunked_to_512)
#print(message_schedule,"\nLenght of message schedule: ",len(message_schedule))




#sigma words added
message_schedule_with_sigmaWords = preprocessing.addSigmaProcessing(message_schedule)



#compression
#using hash values for compressions
binary_of_hexValues = preprocessing.HexToBinary(hash_values)


#final digest
digest = preprocessing.compress(binary_of_hexValues,constants64_binary,message_schedule_with_sigmaWords)

#hash gen
preprocessing.convertAppendHash(digest)







# %%
