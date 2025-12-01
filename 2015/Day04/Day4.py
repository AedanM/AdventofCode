import hashlib
secretKey = "bgvyzdsv"
def getZerosHash(secretKey, numZeros):
    i = 0
    while True:
        secretResult = secretKey + str(i)
        output = (hashlib.md5(secretResult.encode())).hexdigest()
        if(all(x == '0' for x in output[0:numZeros])):
            break
        i += 1
    return i, secretResult

print(getZerosHash(secretKey,5))
print(getZerosHash(secretKey,6))