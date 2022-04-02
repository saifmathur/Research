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
    

#genSHA()

genMod.genModHash()
end=time.time()
print(end-start)

# %%
