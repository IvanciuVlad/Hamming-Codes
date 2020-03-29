def bitCheck(bits):
    valid = ['1', '0']
    for item in bits:
        if item not in valid:
            return 0
    return 1


print("Insert the Hamming code")
data = input()
hammingCode = list(data)
hammingCode.reverse()
if bitCheck(hammingCode):
    print("It's valid")
    r, c, j, error = 0, 0, 0, 0
    dataBits, hammingCode_copy = [], []
    l = len(hammingCode)

    for i in range(l):
        hammingCode[i] = int(hammingCode[i])
        hammingCode_copy.append(hammingCode[i])

    for bitIndex in range(l):
        p = 2 ** c
        if p == bitIndex + 1:
            start = p - 1
            i = start
            bitCoverage = []

            while i < l:
                bitBlock = hammingCode[i:i + p]
                bitCoverage.extend(bitBlock)
                i += 2 * p

            for j in range(1, len(bitCoverage)):
                hammingCode[start] = hammingCode[start] ^ bitCoverage[j]
            dataBits.append(hammingCode[bitIndex])
            c += 1

    dataBits.reverse()
    for i, dataBit in enumerate(dataBits[::-1]):
        error += (dataBit * (2 ** i))
    print(error)
    
else:
    print("Insert a valid string")
