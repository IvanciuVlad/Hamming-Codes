import tkinter
from random import randrange

# Dimensions of the window generated
HEIGHT = 600
WIDTH = 700

# Global variable used for hamming code asa string used in multiple functions
hammingCodeStr = ''

def bitCheck(bits):
    valid = ['1', '0']
    for item in bits:
        if item not in valid:
            return 0
    return 1


def lenghtCheckDecode(bits):
    l = len(bits)
    # 16 is a completely arbitrary limit
    for i in range(2, 16):
        if l == (2 ** i) - 1:
            return 1
    return 0


def lengthCheckEncode(bits):
    l = len(bits)
    # once again, arbitrary number
    for i in range(2, 16):
        if l == 2 ** i - i - 1:
            return 1
    return 0


def encode(data):
    labelString = ''
    dataBits = list(data)
    dataBits.reverse()
    if bitCheck(dataBits) and lengthCheckEncode(dataBits):
        labelString = labelString + "Input was: " + data + "\n"
        labelString = labelString + "It's syntactically correct \n"
        l = len(dataBits)
        hammingCode = []
        r, j, c = 0, 0, 0
        # Since dataBits = 2**r + r + 1
        while (l + r + 1) > (2 ** r):
            r += 1
        for i in range(r + l):
            # All bit positions that are powers of two (have a single 1 bit in the binary form of their position) are parity bits: 1, 2, 4, 8, etc. (1, 10, 100, 1000)
            # All other bit positions, with two or more 1 bits in the binary form of their position, are data bits.
            p = 2 ** c
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
                    bitBlock = hammingCode[i:i + p]
                    bitCoverage.extend(bitBlock)
                    i += 2 * p

                # Calculating each parity bit
                for j in range(len(bitCoverage)):
                    hammingCode[start] = hammingCode[start] ^ bitCoverage[j]
                c += 1

        hammingCode.reverse()
        labelString = labelString + "Encoded: " + ''.join(map(str, hammingCode)) + '\n'
        global hammingCodeStr
        hammingCodeStr = ''.join(map(str, hammingCode))
    else:
        labelString = "Insert a valid string"
    label['text'] = labelString
    entry.delete(0, 'end')
    entry.insert(0, ''.join(map(str, hammingCode)))


def decode(data):
    labelString = ''
    hammingCode = list(data)
    hammingCode.reverse()
    if bitCheck(hammingCode) and lenghtCheckDecode(hammingCode):
        labelString = labelString + "It's syntactically correct\n"
        r, c, j, error = 0, 0, 0, 0
        syndromes, hammingCode_copy, dataBits = [], [], []
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
                while i < l:
                    bitBlock = hammingCode[i:i + p]
                    bitCoverage.extend(bitBlock)
                    i += 2 * p

                for j in range(1, len(bitCoverage)):
                    hammingCode[start] = hammingCode[start] ^ bitCoverage[j]
                syndromes.append(hammingCode[bitIndex])
                c += 1

        # Error detection and correction
        for i, syndrome in enumerate(syndromes[::1]):
            error += (syndrome * (2 ** i))

        if error == 0:
            labelString = labelString + "There is no error in code." + '\n'
        elif error > l:
            labelString = labelString + "Error too complex." + '\n'
        else:
            labelString = labelString + "Bit " + str(error) + " is flipped." + '\n'
            hammingCode_copy[error - 1] ^= 1
            hammingCode_copy.reverse()
            labelString = labelString + 'The correct code is '
            labelString = labelString + ''.join(map(str, hammingCode_copy)) + '\n'
            hammingCode_copy.reverse()

        # To find the original data bits we use the corrected hamming code (if there was an error)
        # Then we use the same process as for finding the control bits but this time we save the data bits into a separate vector
        labelString = labelString + 'The original data bits are '
        c = 0
        for bitIndex in range(l):
            p = 2 ** c
            if p == bitIndex + 1:
                c += 1
            else:
                dataBits.append(hammingCode_copy[bitIndex])
        labelString = labelString + ''.join(map(str, dataBits))

    else:
        labelString = 'Insert a valid string'
    label['text'] = labelString


def generateDataBits(length):
    genBits = ''
    # Generates a random bit code of the length specified by the user and inserts it in the entry
    for i in range(int(length)):
        genBits += str(randrange(2))
    entry.delete(0, 'end')
    entry.insert(0, genBits)


def invertBit(position):
    # Since in python strings are not immutable, we converted it into a list and we invert the bit at the position specified by the user, the new string is inserted in the Entry
    hc = list(hammingCodeStr)
    if hc[int(position) - 1] == "1":
        hc[int(position) - 1] = "0"
    else:
        hc[int(position) - 1] = "1"
    entry.delete(0, 'end')
    entry.insert(0, ''.join(map(str, hc)))


root = tkinter.Tk()

root.title("Hamming codes")

canvas = tkinter.Canvas(root, heigh=HEIGHT, width=WIDTH, bg='#ccffff')
canvas.pack()

frame = tkinter.Frame(root, bg='#b3b3ff', bd=5)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

entry = tkinter.Entry(frame, font=72)
entry.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.4)

label = tkinter.Label(frame, text='Please insert your code', font=72)
label.place(relx=0.0, rely=0.7, relwidth=1.0, relheight=0.4)

encodeButton = tkinter.Button(frame, text='Encode', bg='cyan', fg='red', font=72, command=lambda: encode(entry.get()))
encodeButton.place(relx=0.0, rely=0.3, relwidth=0.5, relheight=0.2)

decodeButton = tkinter.Button(frame, text='Decode', bg='cyan', fg='red', font=72, command=lambda: decode(entry.get()))
decodeButton.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)

generateBits = tkinter.Button(frame, text='Generate', bg='cyan', fg='red', font=72, command=lambda: generateDataBits(entry.get()))
generateBits.place(relx=0.0, rely=0.5, relwidth=0.5, relheight=0.2)

changeBit = tkinter.Button(frame, text='Change bit', bg='cyan', fg='red', font=72, command=lambda: invertBit(entry.get()))
changeBit.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.2)

root.mainloop()