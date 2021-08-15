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

    #keep count of years by increments of 5
    twoTo1995 = ['1992', '1993', '1994', '1995']
    sixTo2000 = ['1996', '1997', '1998', '1999', '2000']
    oneTo2005 = ['2001', '2002', '2003', '2004', '2005']
    sixTo2010 = ['2006', '2007', '2008', '2009', '2010']
    elevenTo2015 = ['2011', '2012', '2013', '2014', '2015']

    #used to keep count of fires in each region
    w = sW = mW = sE = nE = 0

    #used to keep count of fires in each region for that year
    west1992To1995 = west1996To2000 = west2001To2005 = west2006To2010 = west2011To2015 = 0
    southWest1992To1995 = southWest1996To2000 = southWest2001To2005 = southWest2006To2010 = southWest2011To2015 = 0
    midWest1992To1995 = midWest1996To2000 = midWest2001To2005 = midWest2006To2010 = midWest2011To2015 = 0
    southEast1992To1995 = southEast1996To2000 = southEast2001To2005 = southEast2006To2010 = southEast2011To2015 = 0
    northEast1992To1995 = northEast1996To2000 = northEast2001To2005 = northEast2006To2010 = northEast2011To2015 = 0

    resultRows = []
    with open('fireData.csv', 'r') as readOBJ:
        csvReader = reader(readOBJ)
        resultRows.append(list(csvReader))
        #print(resultRows)

    #count occurrences of each region and years
    for rows in resultRows:
        for row in rows:
            if row[1] in west:
                w += 1
                if row[3] in twoTo1995:
                    west1992To1995 += 1
                elif row[3] in sixTo2000:
                    west1996To2000 += 1
                elif row[3] in oneTo2005:
                    west2001To2005 += 1
                elif row[3] in sixTo2010:
                    west2006To2010 += 1
                elif row[3] in elevenTo2015:
                    west2011To2015 += 1
            elif row[1] in southWest:
                sW += 1
                if row[3] in twoTo1995:
                    southWest1992To1995 += 1
                elif row[3] in sixTo2000:
                    southWest1996To2000 += 1
                elif row[3] in oneTo2005:
                    southWest2001To2005 += 1
                elif row[3] in sixTo2010:
                    southWest2006To2010 += 1
                elif row[3] in elevenTo2015:
                    southWest2011To2015 += 1
            elif row[1] in midWest:
                mW += 1
                if row[3] in twoTo1995:
                    midWest1992To1995 += 1
                elif row[3] in sixTo2000:
                    midWest1996To2000 += 1
                elif row[3] in oneTo2005:
                    midWest2001To2005 += 1
                elif row[3] in sixTo2010:
                    midWest2006To2010 += 1
                elif row[3] in elevenTo2015:
                    midWest2011To2015 += 1
            elif row[1] in southEast:
                sE += 1
                if row[3] in twoTo1995:
                    southEast1992To1995 += 1
                elif row[3] in sixTo2000:
                    southEast1996To2000 += 1
                elif row[3] in oneTo2005:
                    southEast2001To2005 += 1
                elif row[3] in sixTo2010:
                    southEast2006To2010 += 1
                elif row[3] in elevenTo2015:
                    southEast2011To2015 += 1
            elif row[1] in northEast:
                nE += 1
                if row[3] in twoTo1995:
                    northEast1992To1995 += 1
                elif row[3] in sixTo2000:
                    northEast1996To2000 += 1
                elif row[3] in oneTo2005:
                    northEast2001To2005 += 1
                elif row[3] in sixTo2010:
                    northEast2006To2010 += 1
                elif row[3] in elevenTo2015:
                    northEast2011To2015 += 1
            else:
                x = 0
    totalWest = [west1992To1995, west1996To2000, west2001To2005, west2006To2010, west2011To2015]
    totalsouthWest = [southWest1992To1995, southWest1996To2000, southWest2001To2005, southWest2006To2010, southWest2011To2015]
    totalmidWest = [midWest1992To1995, midWest1996To2000, midWest2001To2005, midWest2006To2010, midWest2011To2015]
    totalsouthEast = [southEast1992To1995, southEast1996To2000, southEast2001To2005, southEast2006To2010, southEast2011To2015]
    totalnorthEast = [northEast1992To1995, northEast1996To2000, northEast2001To2005, northEast2006To2010, northEast2011To2015]

    plotHistogram(totalWest, totalsouthWest, totalmidWest, totalsouthEast, totalnorthEast)

def plotHistogram(west, southwest, midwest, southeast, northeast):
    data = [west, southwest, midwest, southeast, northeast]
    xAxisLabels = ['1992-1995', '1996-2000', '2001-2005', '2006-2010', '2011-2015']

    X = np.arange(5)
    #fig = plt.figure() --old way to plot that can't add values to x and y axis
    #ax = fig.add_axes([0,0,1,1])

    fig, ax = plt.subplots()

    ax.bar(X + 0.00, data[0], color='b', width=0.2)
    ax.bar(X + 0.2, data[1], color='k', width=0.2)
    ax.bar(X + 0.4, data[2], color='r', width=0.2)
    ax.bar(X + 0.6, data[3], color='y', width=0.2)
    ax.bar(X + 0.8, data[4], color='g', width=0.2)

    #ax.set_xticks(X)

    plt.show()

def generatePredictionData(frame):
    print(frame)

if __name__ == '__main__':
    print("Beginning")
    readDataIntoHistogram()