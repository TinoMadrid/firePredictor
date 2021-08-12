from csv import reader
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def readDataIntoHistogram():
    # regions of the US
    west = ['WA', 'OR', 'CA', 'NV', 'ID', 'MT', 'WY', 'UT', 'CO', 'HI', 'AK']
    southWest = ['AZ', 'NM', 'TX', 'OK']
    midWest = ['ND', 'SD', 'NE', 'KS', 'MO', 'IA', 'MN', 'WI', 'IL', 'IN', 'MI', 'OH']
    southEast = ['AR', 'LA', 'MS', 'AL', 'TN', 'KY', 'WV', 'VA', 'NC', 'SC', 'GA', 'FL']
    northEast = ['ME', 'NH', 'VT', 'NY', 'PA', 'MD', 'DE', 'NJ', 'CT', 'RI', 'MA']

    #used to keep count of fires in each region
    w = sW = mW = sE = nE = 0

    resultRows = []
    with open('fireData.csv', 'r') as readOBJ:
        csvReader = reader(readOBJ)
        resultRows.append(list(csvReader))


    for rows in resultRows:
        for row in rows:
            if row[1] in west:
                w += 1
            elif row[1] in southWest:
                sW += 1
            elif row[1] in midWest:
                mW += 1
            elif row[1] in southEast:
                sE += 1
            elif row[1] in northEast:
                nE += 1
            else:
                x = 0
    plotHistogram(w, sW, mW, sE, nE)

def plotHistogram(west, southwest, midwest, southeast, northeast):
    valueList = [west, southwest, midwest, southeast, northeast]

    xAxisLabels = ['West', 'SouthWest', 'MidWest', 'SouthEast', 'NorthEast']

    plt.bar(xAxisLabels, valueList)
    plt.show()

if __name__ == '__main__':
    print("Beginning")
    readDataIntoHistogram()