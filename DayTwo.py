import Util
import numpy as np
import pandas as pd

def getData(path):
    data = pd.read_csv(path, header=None, squeeze=True).to_numpy()
    return data

def processRow(row):
    return row.split(' ')

def processData(data):
    processed_data = []
    for row in data:
        processed_data.append(processRow(row))
    return processed_data

def getLocation(data):
    x = 0
    y = 0
    for (direction, length) in data:
        if direction == 'forward':
            x += int(length)
        elif direction == 'down':
            y += int(length)
        elif direction == 'up':
            y -= int(length)

    return x, y

def main():
    # Part one test
    data = getData('data/2-part-1-test.txt')
    data = processData(data)
    x, y = getLocation(data)
    prod = x * y
    assert x == 15
    assert y == 10
    assert prod == 150

    # Part one
    data = getData('data/2-part-1.txt')
    data = processData(data)
    x, y = getLocation(data)
    prod = x * y
    print('Part one:', prod)

    return 0

if __name__ == '__main__':
    main()