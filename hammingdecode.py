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
    controlBits, hammingCode_copy = [], []
    l = len(hammingCode)

    # Creating a copy and changing the data type to integer
    for i in range(l):
        hammingCode[i] = int(hammingCode[i])
        hammingCode_copy.append(hammingCode[i])

    # We take each bit in the list and identify the parity bits
    for bitIndex in range(l):
        p = 2 ** c
        if p == bitIndex + 1:
            start = p - 1
            i = start
            bitCoverage = []

            # For each control bit, we recalculate the parity, same as for encoding
            # We save the control bits in controlBits
            while i < l:
                bitBlock = hammingCode[i:i + p]
                bitCoverage.extend(bitBlock)
                i += 2 * p

            for j in range(1, len(bitCoverage)):
                hammingCode[start] = hammingCode[start] ^ bitCoverage[j]
            controlBits.append(hammingCode[bitIndex])
            c += 1

    # Error detection and correction
    for i, controlBit in enumerate(controlBits[::1]):
        error += (controlBit * (2 ** i))

    if error == 0:
        print("There is no error in the code")
    elif error > l:
        print("Error too complex")
    else:
        print("Bit ", error, " is flipped")
        hammingCode_copy[error - 1] ^= 1
        hammingCode_copy.reverse()
        print("The correct code is ", hammingCode_copy)
    
else:
    print("Insert a valid string")
