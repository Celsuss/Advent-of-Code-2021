import numpy as np

def getData(path):
    data = np.genfromtxt(path, dtype='str')
    return data

def convertToMatrix(data):
    matrix = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):
        for j, val in enumerate(data[i]):
            matrix[i][j] = val
    return matrix

def getGamma(data):
    gamma = []
    for row in data:
        if np.count_nonzero(row) > len(row) / 2:
            gamma.append(1)
        else:
            gamma.append(0)
    return np.array(gamma)

def getEpsilon(gamma):
    epsilon = np.zeros((len(gamma)))
    for i in range(len(gamma)):
        if gamma[i] == 1:
            epsilon[i] = 0
        else:
            epsilon[i] = 1
    return epsilon

def getValuesWithMatchingBit(data, bit, bit_index):
    values = []
    for row in data:
        if row[bit_index] == bit:
            values.append(row)
    return values

def getOxygen(data, bit_index=0):
    data_rot = np.rot90(data, -1)
    row = data_rot[bit_index]

    # FInd most common bit
    if np.count_nonzero(row) >= len(row) / 2:
        most_common_bit = 1
    else:
        most_common_bit = 0

    # Keep values with most common bit
    data = getValuesWithMatchingBit(data, most_common_bit, bit_index)

    # Repeat until one value remains
    if len(data) > 1:
        return getOxygen(data, bit_index + 1)
    
    return data[0]

def getCo2(data, bit_index=0):
    data_rot = np.rot90(data, -1)
    row = data_rot[bit_index]

    # FInd most common bit
    if np.count_nonzero(row) < len(row) / 2:
        most_common_bit = 1
    else:
        most_common_bit = 0

    # Keep values with most common bit
    data = getValuesWithMatchingBit(data, most_common_bit, bit_index)

    # Repeat until one value remains
    if len(data) > 1:
        return getCo2(data, bit_index + 1)
    
    return data[0]

def convertBinaryToDecimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += binary[i] * 2**(len(binary) - i - 1)
    return decimal

def printMatrix(matrix):
    for row in matrix:
        print(row)

def main():
    # Part one test
    data = getData('data/3-test.txt')
    data = convertToMatrix(data)
    data = np.rot90(data, -1)    
    gamma_binary = getGamma(data)
    gamma = convertBinaryToDecimal(gamma_binary)
    assert gamma == 22
    epsilon_binary = getEpsilon(gamma_binary)
    epsilon = convertBinaryToDecimal(epsilon_binary)
    assert epsilon == 9
    power = gamma * epsilon
    assert power == 198

    # Part one
    data = getData('data/3.txt')
    data = convertToMatrix(data)
    data = np.rot90(data, -1)
    gamma = getGamma(data)
    epsilon = getEpsilon(gamma)
    gamma = convertBinaryToDecimal(gamma)
    epsilon = convertBinaryToDecimal(epsilon)
    power = gamma * epsilon
    print('Part one:', power)

    # Part two test
    data = getData('data/3-test.txt')
    data = convertToMatrix(data)
    oxygen = getOxygen(data)
    oxygen = convertBinaryToDecimal(oxygen)
    assert oxygen == 23
    co2 = getCo2(data)
    co2 = convertBinaryToDecimal(co2)
    assert co2 == 10
    life = oxygen * co2
    assert life == 230

    # Part two
    data = getData('data/3.txt')
    data = convertToMatrix(data)
    oxygen = getOxygen(data)
    oxygen = convertBinaryToDecimal(oxygen)
    co2 = getCo2(data)
    co2 = convertBinaryToDecimal(co2)
    life = oxygen * co2
    print('Part two:', life)

    return 0

if __name__ == '__main__':
    main()