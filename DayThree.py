import numpy as np

def getData(path):
    data = np.genfromtxt(path, dtype='str')
    return data

def convertToMatrix(data):
    matrix = np.zeros((len(data[0]), len(data)))
    for i in range(len(data)):
        for j, val in enumerate(data[i]):
            matrix[j][i] = val
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

def convertBinaryToDecimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += binary[i] * 2**(len(binary) - i - 1)
    return decimal

def main():
    # Part one test
    data = getData('data/3-test.txt')
    data = convertToMatrix(data)
    gamma = getGamma(data)
    epsilon = getEpsilon(gamma)
    gamma = convertBinaryToDecimal(gamma)
    epsilon = convertBinaryToDecimal(epsilon)
    power = gamma * epsilon
    assert gamma == 22
    assert epsilon == 9
    assert power == 198

    # Part one
    data = getData('data/3.txt')
    data = convertToMatrix(data)
    gamma = getGamma(data)
    epsilon = getEpsilon(gamma)
    gamma = convertBinaryToDecimal(gamma)
    epsilon = convertBinaryToDecimal(epsilon)
    power = gamma * epsilon
    print('Part one:', power)



    return 0

if __name__ == '__main__':
    main()