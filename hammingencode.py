def bitCheck(bits):
    valid = ['1', '0']
    for item in bits:
        if item not in valid:
            return 0
    return 1

print('Insert the data bits')
data = input()
dataBits = list(data)
dataBits.reverse()
if bitCheck(dataBits):
    print("It's valid")
    l = len(dataBits)
    hammingCode = []
    r, j, c = 0, 0, 0
    # Since dataBits = 2**r + r + 1
    while (l + r + 1) > (2**r):
        r += 1
    for i in range(r + l):
        # All bit positions that are powers of two (have a single 1 bit in the binary form of their position) are parity bits: 1, 2, 4, 8, etc. (1, 10, 100, 1000)
        # All other bit positions, with two or more 1 bits in the binary form of their position, are data bits.
        p = 2**c
        if (i + 1) == p:
            hammingCode.append(0)
            c += 1
        else:
            hammingCode.append(int(dataBits[j]))
            j += 1

    c = 0  # resetting counter
    l = len(hammingCode)

    # Taking each parity bit and gathering the data bits covered by the it
    for bitIndex in range(l):
         p = 2 ** c

         # Each data bit is included in a unique set of 2 or more parity bits, as determined by the binary form of its bit position
         # In general each parity bit covers all bits where the bitwise AND of the parity position and the bit position is non-zero
         #  if you have m parity bits, it can cover bits from 1 up to 2**m − 1
         #  If we subtract out the parity bits, we are left with 2**m − m − 1 bits we can use for the data
         if p == bitIndex + 1:
            start = p - 1
            i = start
            bitCoverage = []

            # Adding the data bits covered by bitIndex parity bit
            while i < l:
                bitBlock = hammingCode[i:i+p]
                bitCoverage.extend(bitBlock)
                i += 2*p

            # Calculating each parity bit
            for j in range(len(bitCoverage)):
                hammingCode[start] = hammingCode[start] ^ bitCoverage[j]
            c += 1

    hammingCode.reverse()
    print("Resulting Hamming Code is: ", end='')
    print(''.join(map(str, hammingCode)))

else:
    print("Insert a valid string")