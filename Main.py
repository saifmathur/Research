#%%
import time
start = time.time()
from Preprocessing import Preprocessing
from modSHA import ModSHA, GenModHash
from Tools import PreProcessing
preprocessing = PreProcessing()
mod = ModSHA()
genMod = GenModHash()
message_schedule, hash_values, constants64_binary = Preprocessing().preprocess()
binary_of_hexValues = preprocessing.HexToBinary(hash_values)


def genSHA():
    #sigma words added
    message_schedule_with_sigmaWords = preprocessing.addSigmaProcessing(message_schedule)
    #compression
    #using hash values for compressions
    binary_of_hexValues = preprocessing.HexToBinary(hash_values)
    #final digest
    digest = preprocessing.compress(binary_of_hexValues,constants64_binary,message_schedule_with_sigmaWords)
    #hash
    preprocessing.convertAppendHash(digest)
    

genSHA()
genMod.genModHash()
end=time.time()
print("Time to Hash: ",end-start)

# %%
import time
start = time.time()
import hashlib
import requests
a_string = requests.get('https://baconipsum.com/api/?type=meat-and-filler&paras=5&format=text').text
hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)
end = time.time()
print(end-start)
# %%

# 2.0325841903686523
# 1.147935152053833
