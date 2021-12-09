import pandas as pd
import requests
import os

# BASE_URL = 'https://adventofcode.com/2021/day/1/input'
BASE_URL = 'https://adventofcode.com/2021/day/'
DATA_PATH = './data/'

def getURLFromDay(day):
    return BASE_URL + str(day) + '/input'

def getDataFromURL(day):
    return requests.get(getURLFromDay(day)).text

def saveDataToFile(day, data):
    fileName = DATA_PATH + str(day) + '.txt'
    with open(fileName, 'w') as f:
        f.write(data)

def getDataFromFile(day):
    fileName = DATA_PATH + str(day) + '.txt'
    if not os.path.isfile(fileName):
        return None

    return pd.read_csv(fileName, header=None, squeeze=True).values.tolist()
    # with open(fileName, 'r') as f:
    #     return f.read()

def getData(day):
    data = getDataFromFile(day)

    if data is None:
        data = getDataFromURL(day)
        saveDataToFile(day, data)

    return data