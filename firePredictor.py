from pandas import read_table
from csv import reader
import numpy as np
import matplotlib.pyplot as plt

def readDataIntoHistogram():
    # regions of the US
    west = ['WA', 'OR', 'CA', 'NV', 'ID', 'MT', 'WY', 'UT', 'CO', 'HI', 'AK']
    southWest = ['AZ', 'NM', 'TX', 'OK']
    midWest = ['ND', 'SD', 'NE', 'KS', 'MO', 'IA', 'MN', 'WI', 'IL', 'IN', 'MI', 'OH']
    southEast = ['AR', 'LA', 'MS', 'AL', 'TN', 'KY', 'WV', 'VA', 'NC', 'SC', 'GA', 'FL']
    northEast = ['ME', 'NH', 'VT', 'NY', 'PA', 'MD', 'DE', 'NJ', 'CT', 'RI', 'MA']

    regions = [west, southWest, midWest, southEast, northEast]

    #used to keep count of fires in each region
    w = sW = mW = sE = nE = 0

    with open('fireData.csv', 'r') as readOBJ:
        csvReader = reader(readOBJ)
        listOfRows = list(csvReader)
        print(listOfRows)



if __name__ == '__main__':
    print("Beginning")
    readDataIntoHistogram()