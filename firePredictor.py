import tkinter
from csv import reader

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button as Buttons
import pandas as pd
from sklearn.linear_model import LinearRegression
import mplcursors
from sklearn.metrics import max_error

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
    X = np.arange(5)
    fig, ax = plt.subplots()

    ax.bar(X + 0.1, data[0], color='b', width=0.2)
    ax.bar(X + 0.3, data[1], color='k', width=0.2)
    ax.bar(X + 0.4, data[2], color='r', width=0.2)
    ax.bar(X + 0.5, data[3], color='y', width=0.2)
    ax.bar(X + 0.6, data[4], color='g', width=0.2)

    ax.set_xticks([0,1,2,3,4])
    ax.set_xticklabels(['1992-1995', '1996-2000', '2001-2005', '2006-2010', '2011-2015'])
    ax.set_ylabel('Fire Outbreak Count')
    ax.set_xlabel('Years')
    ax.set_title('Wildfire Outbreak by Years')

    #legend of existing data
    colors = {'west':'blue', 'southwest':'black', 'midwest':'red', 'southeast':'yellow', 'northeast':'green'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)

    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)

    @cursor.connect("add")
    def on_add(se):
        x, y, width, height = se.artist[se.target.index].get_bbox().bounds
        height = round(height)
        se.annotation.set(text=height,
                           position=(0, 20), anncoords="offset points")
        se.annotation.xy = (x + width / 2, y + height)

    axes = plt.axes([0.88, 0.000001, 0.11, 0.075])
    bnext = Buttons(axes, 'Predictions', color="yellow")
    bnext.on_clicked(mainWindow)
    plt.show()

def event():
    west, southwest, midwest, southeast, northeast = precursorOfPredictionData()
    futureFireGraph(west, southwest, midwest, southeast, northeast)

def event10Year():
    west, southwest, midwest, southeast, northeast = precursorOfPredictionData10Year()
    futureFireGraph10Year(west, southwest, midwest, southeast, northeast)

def event15Year():
    west, southwest, midwest, southeast, northeast = precursorOfPredictionData15Year()
    futureFireGraph15Year(west, southwest, midwest, southeast, northeast)

def mainWindow(e):
    print("Dashboard window here")
    menu = tkinter.Tk()
    menu.title("Future Year Increments")
    menu.geometry('450x200')
    lbl = tkinter.Label(menu, text="Select years to see the projected fire out comes for each region of the U.S.")
    lbl.grid(column=0, row=0)

    btn = tkinter.Button(menu, text="2022-2027", command=event)
    btn.grid(column=0, row=4)

    btn = tkinter.Button(menu, text="2022-2032", command=event10Year)
    btn.grid(column=0, row=5)

    btn = tkinter.Button(menu, text="2022-2037", command=event15Year)
    btn.grid(column=0, row=6)

    menu.mainloop()

def precursorOfPredictionData():
    westRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [14941.75, 14941.75, 14941.75, 14941.75, 17975.2, 17975.2, 17975.2, 17975.2, 17975.2, 17461.4,
                       17461.4, 17461.4, 17461.4, 17461.4, 17151.6, 17151.6, 17151.6, 17151.6, 17151.6, 16751.6, 16751.6, 16751.6, 16751.6, 16751.6]
    }
    SouthWestRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [3931.75, 3931.75, 3931.75, 3931.75, 5203, 5203, 5203, 5203, 5203, 5632, 5632, 5632, 5632, 5632, 9803.2, 9803.2, 9803.2, 9803.2, 9803.2, 15460.4, 15460.4, 15460.4, 15460.4, 15460.4,]
    }
    MidWestRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [1293.75, 1293.75, 1293.75, 1293.75, 3131.4, 3131.4, 3131.4, 3131.4, 3131.4, 3681.2, 3681.2, 3681.2, 3681.2, 3681.2, 3401.8, 3401.8, 3401.8, 3401.8, 3401.8, 5995.2, 5995.2, 5995.2, 5995.2, 5995.2]
    }
    SouthEastRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [1637.25, 1637.25, 1637.25, 1637.25, 9159, 9159, 9159, 9159, 9159, 9580.8, 9580.8, 9580.8, 9580.8, 9580.8, 5782.8, 5782.8, 5782.8, 5782.8, 5782.8, 18028.4, 18028.4, 18028.4, 18028.4, 18028.4]
    }
    NorthEastRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [444.25, 444.25, 444.25, 444.25, 106.6, 106.6, 106.6, 106.6, 106.6, 111.4, 111.4, 111.4, 111.4, 111.4, 143, 143, 143, 143, 143, 2212.2, 2212.2, 2212.2, 2212.2, 2212.2]
    }

    # convert dictionaries to pandas dataframe
    westDF = pd.DataFrame(westRegionFrame)
    SouthWestDF = pd.DataFrame(SouthWestRegionFrame)
    MidWestDF = pd.DataFrame(MidWestRegionFrame)
    SouthEastDF = pd.DataFrame(SouthEastRegionFrame)
    NorthEastDF = pd.DataFrame(NorthEastRegionFrame)

    # west
    x_west = westDF['Years'].values.tolist()
    year_west = np.array(x_west)
    year_west = year_west.reshape((-1,1))
    y_west = westDF['Fire Count'].values
    fire_west = np.array(y_west)
    fire_west = fire_west.reshape((-1,1))

    # southwest
    x_southwest = SouthWestDF['Years'].values.tolist()
    year_southwest = np.array(x_southwest)
    year_southwest = year_southwest.reshape((-1,1))
    y_southwest = SouthWestDF['Fire Count'].values
    fire_southwest = np.array(y_southwest)
    fire_southwest = fire_southwest.reshape((-1,1))

    # midwest
    x_midwest = MidWestDF['Years'].values.tolist()
    year_midwest = np.array(x_midwest)
    year_midwest = year_midwest.reshape((-1,1))
    y_midwest = MidWestDF['Fire Count'].values
    fire_midwest = np.array(y_midwest)
    fire_midwest = fire_midwest.reshape((-1,1))

    # southeast
    x_southeast = SouthEastDF['Years'].values.tolist()
    year_southeast = np.array(x_southeast)
    year_southeast = year_southeast.reshape((-1,1))
    y_southeast = SouthEastDF['Fire Count'].values
    fire_southeast = np.array(y_southeast)
    fire_southeast = fire_southeast.reshape((-1,1))

    # northeast
    x_northeast = NorthEastDF['Years'].values.tolist()
    year_northeast = np.array(x_northeast)
    year_northeast = year_northeast.reshape((-1,1))
    y_northeast = NorthEastDF['Fire Count'].values
    fire_northeast = np.array(y_northeast)
    fire_northeast = fire_northeast.reshape((-1,1))

    west_reg = LinearRegression().fit(year_west, fire_west)
    southwest_reg = LinearRegression().fit(year_southwest, fire_southwest)
    midwest_reg = LinearRegression().fit(year_midwest, fire_midwest)
    southeast_reg = LinearRegression().fit(year_southeast, fire_southeast)
    northeast_reg = LinearRegression().fit(year_northeast, fire_northeast)

    #accuracy verification
    y_west_predict = []
    for x in range(2022, 2046):
        y_west_predict.append(west_reg.predict([[x]]))
    ywp = np.array(y_west_predict)
    ywp = ywp.reshape((-1,1))
    print(max_error(y_west, ywp))

    # future fire prediction containers
    westFuture = []
    southWestFuture = []
    midWestFuture = []
    southEastFuture = []
    northEastFuture = []

    for i in range(2022, 2027):
        westFuture.append(west_reg.predict([[i]]))
        southWestFuture.append(southwest_reg.predict([[i]]))
        midWestFuture.append(midwest_reg.predict([[i]]))
        southEastFuture.append(southeast_reg.predict([[i]]))
        northEastFuture.append(northeast_reg.predict([[i]]))
    return westFuture, southWestFuture, midWestFuture, southEastFuture, northEastFuture

def precursorOfPredictionData10Year():
    westRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [14941.75, 14941.75, 14941.75, 14941.75, 17975.2, 17975.2, 17975.2, 17975.2, 17975.2, 17461.4,
                       17461.4, 17461.4, 17461.4, 17461.4, 17151.6, 17151.6, 17151.6, 17151.6, 17151.6, 16751.6, 16751.6, 16751.6, 16751.6, 16751.6]
    }
    SouthWestRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [3931.75, 3931.75, 3931.75, 3931.75, 5203, 5203, 5203, 5203, 5203, 5632, 5632, 5632, 5632, 5632, 9803.2, 9803.2, 9803.2, 9803.2, 9803.2, 15460.4, 15460.4, 15460.4, 15460.4, 15460.4,]
    }
    MidWestRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [1293.75, 1293.75, 1293.75, 1293.75, 3131.4, 3131.4, 3131.4, 3131.4, 3131.4, 3681.2, 3681.2, 3681.2, 3681.2, 3681.2, 3401.8, 3401.8, 3401.8, 3401.8, 3401.8, 5995.2, 5995.2, 5995.2, 5995.2, 5995.2]
    }
    SouthEastRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [1637.25, 1637.25, 1637.25, 1637.25, 9159, 9159, 9159, 9159, 9159, 9580.8, 9580.8, 9580.8, 9580.8, 9580.8, 5782.8, 5782.8, 5782.8, 5782.8, 5782.8, 18028.4, 18028.4, 18028.4, 18028.4, 18028.4]
    }
    NorthEastRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [444.25, 444.25, 444.25, 444.25, 106.6, 106.6, 106.6, 106.6, 106.6, 111.4, 111.4, 111.4, 111.4, 111.4, 143, 143, 143, 143, 143, 2212.2, 2212.2, 2212.2, 2212.2, 2212.2]
    }

    # convert dictionaries to pandas dataframe
    westDF = pd.DataFrame(westRegionFrame)
    SouthWestDF = pd.DataFrame(SouthWestRegionFrame)
    MidWestDF = pd.DataFrame(MidWestRegionFrame)
    SouthEastDF = pd.DataFrame(SouthEastRegionFrame)
    NorthEastDF = pd.DataFrame(NorthEastRegionFrame)

    # west
    x_west = westDF['Years'].values.tolist()
    year_west = np.array(x_west)
    year_west = year_west.reshape((-1,1))
    y_west = westDF['Fire Count'].values
    fire_west = np.array(y_west)
    fire_west = fire_west.reshape((-1,1))

    # southwest
    x_southwest = SouthWestDF['Years'].values.tolist()
    year_southwest = np.array(x_southwest)
    year_southwest = year_southwest.reshape((-1,1))
    y_southwest = SouthWestDF['Fire Count'].values
    fire_southwest = np.array(y_southwest)
    fire_southwest = fire_southwest.reshape((-1,1))

    # midwest
    x_midwest = MidWestDF['Years'].values.tolist()
    year_midwest = np.array(x_midwest)
    year_midwest = year_midwest.reshape((-1,1))
    y_midwest = MidWestDF['Fire Count'].values
    fire_midwest = np.array(y_midwest)
    fire_midwest = fire_midwest.reshape((-1,1))

    # southeast
    x_southeast = SouthEastDF['Years'].values.tolist()
    year_southeast = np.array(x_southeast)
    year_southeast = year_southeast.reshape((-1,1))
    y_southeast = SouthEastDF['Fire Count'].values
    fire_southeast = np.array(y_southeast)
    fire_southeast = fire_southeast.reshape((-1,1))

    # northeast
    x_northeast = NorthEastDF['Years'].values.tolist()
    year_northeast = np.array(x_northeast)
    year_northeast = year_northeast.reshape((-1,1))
    y_northeast = NorthEastDF['Fire Count'].values
    fire_northeast = np.array(y_northeast)
    fire_northeast = fire_northeast.reshape((-1,1))

    west_reg = LinearRegression().fit(year_west, fire_west)
    southwest_reg = LinearRegression().fit(year_southwest, fire_southwest)
    midwest_reg = LinearRegression().fit(year_midwest, fire_midwest)
    southeast_reg = LinearRegression().fit(year_southeast, fire_southeast)
    northeast_reg = LinearRegression().fit(year_northeast, fire_northeast)

    # future fire prediction containers
    westFuture = []
    southWestFuture = []
    midWestFuture = []
    southEastFuture = []
    northEastFuture = []

    for i in range(2022, 2032):
        westFuture.append(west_reg.predict([[i]]))
        southWestFuture.append(southwest_reg.predict([[i]]))
        midWestFuture.append(midwest_reg.predict([[i]]))
        southEastFuture.append(southeast_reg.predict([[i]]))
        northEastFuture.append(northeast_reg.predict([[i]]))
    return westFuture, southWestFuture, midWestFuture, southEastFuture, northEastFuture

def precursorOfPredictionData15Year():
    westRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [14941.75, 14941.75, 14941.75, 14941.75, 17975.2, 17975.2, 17975.2, 17975.2, 17975.2, 17461.4,
                       17461.4, 17461.4, 17461.4, 17461.4, 17151.6, 17151.6, 17151.6, 17151.6, 17151.6, 16751.6, 16751.6, 16751.6, 16751.6, 16751.6]
    }
    SouthWestRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [3931.75, 3931.75, 3931.75, 3931.75, 5203, 5203, 5203, 5203, 5203, 5632, 5632, 5632, 5632, 5632, 9803.2, 9803.2, 9803.2, 9803.2, 9803.2, 15460.4, 15460.4, 15460.4, 15460.4, 15460.4,]
    }
    MidWestRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [1293.75, 1293.75, 1293.75, 1293.75, 3131.4, 3131.4, 3131.4, 3131.4, 3131.4, 3681.2, 3681.2, 3681.2, 3681.2, 3681.2, 3401.8, 3401.8, 3401.8, 3401.8, 3401.8, 5995.2, 5995.2, 5995.2, 5995.2, 5995.2]
    }
    SouthEastRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [1637.25, 1637.25, 1637.25, 1637.25, 9159, 9159, 9159, 9159, 9159, 9580.8, 9580.8, 9580.8, 9580.8, 9580.8, 5782.8, 5782.8, 5782.8, 5782.8, 5782.8, 18028.4, 18028.4, 18028.4, 18028.4, 18028.4]
    }
    NorthEastRegionFrame = {
        'Years': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                  2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Fire Count': [444.25, 444.25, 444.25, 444.25, 106.6, 106.6, 106.6, 106.6, 106.6, 111.4, 111.4, 111.4, 111.4, 111.4, 143, 143, 143, 143, 143, 2212.2, 2212.2, 2212.2, 2212.2, 2212.2]
    }

    # convert dictionaries to pandas dataframe
    westDF = pd.DataFrame(westRegionFrame)
    SouthWestDF = pd.DataFrame(SouthWestRegionFrame)
    MidWestDF = pd.DataFrame(MidWestRegionFrame)
    SouthEastDF = pd.DataFrame(SouthEastRegionFrame)
    NorthEastDF = pd.DataFrame(NorthEastRegionFrame)

    # west
    x_west = westDF['Years'].values.tolist()
    year_west = np.array(x_west)
    year_west = year_west.reshape((-1,1))
    y_west = westDF['Fire Count'].values
    fire_west = np.array(y_west)
    fire_west = fire_west.reshape((-1,1))

    # southwest
    x_southwest = SouthWestDF['Years'].values.tolist()
    year_southwest = np.array(x_southwest)
    year_southwest = year_southwest.reshape((-1,1))
    y_southwest = SouthWestDF['Fire Count'].values
    fire_southwest = np.array(y_southwest)
    fire_southwest = fire_southwest.reshape((-1,1))

    # midwest
    x_midwest = MidWestDF['Years'].values.tolist()
    year_midwest = np.array(x_midwest)
    year_midwest = year_midwest.reshape((-1,1))
    y_midwest = MidWestDF['Fire Count'].values
    fire_midwest = np.array(y_midwest)
    fire_midwest = fire_midwest.reshape((-1,1))

    # southeast
    x_southeast = SouthEastDF['Years'].values.tolist()
    year_southeast = np.array(x_southeast)
    year_southeast = year_southeast.reshape((-1,1))
    y_southeast = SouthEastDF['Fire Count'].values
    fire_southeast = np.array(y_southeast)
    fire_southeast = fire_southeast.reshape((-1,1))

    # northeast
    x_northeast = NorthEastDF['Years'].values.tolist()
    year_northeast = np.array(x_northeast)
    year_northeast = year_northeast.reshape((-1,1))
    y_northeast = NorthEastDF['Fire Count'].values
    fire_northeast = np.array(y_northeast)
    fire_northeast = fire_northeast.reshape((-1,1))

    west_reg = LinearRegression().fit(year_west, fire_west)
    southwest_reg = LinearRegression().fit(year_southwest, fire_southwest)
    midwest_reg = LinearRegression().fit(year_midwest, fire_midwest)
    southeast_reg = LinearRegression().fit(year_southeast, fire_southeast)
    northeast_reg = LinearRegression().fit(year_northeast, fire_northeast)

    # future fire prediction containers
    westFuture = []
    southWestFuture = []
    midWestFuture = []
    southEastFuture = []
    northEastFuture = []

    for i in range(2022, 2037):
        westFuture.append(west_reg.predict([[i]]))
        southWestFuture.append(southwest_reg.predict([[i]]))
        midWestFuture.append(midwest_reg.predict([[i]]))
        southEastFuture.append(southeast_reg.predict([[i]]))
        northEastFuture.append(northeast_reg.predict([[i]]))
    return westFuture, southWestFuture, midWestFuture, southEastFuture, northEastFuture

def futureFireGraph(w, sw, mw, se, ne):
    data = [sum(w), sum(sw), sum(mw), sum(se), sum(ne)]
    data = np.array(data).flatten()
    X = np.arange(1)
    fig, ax = plt.subplots()

    ax.bar(X + 0.1, data[0], color='b', width=0.2)
    ax.bar(X + 0.3, data[1], color='k', width=0.2)
    ax.bar(X + 0.4, data[2], color='r', width=0.2)
    ax.bar(X + 0.5, data[3], color='y', width=0.2)
    ax.bar(X + 0.6, data[4], color='g', width=0.2)

    ax.set_xticks([0, 0.7])
    ax.set_xticklabels(['2022', '2027'])
    ax.set_ylabel('Fire Outbreak Count')
    ax.set_xlabel('Years')
    ax.set_title('Predicted Fire Outbreak Next 5 Years')

    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)
    @cursor.connect("add")
    def on_add(se):
        x, y, width, height = se.artist[se.target.index].get_bbox().bounds
        height = round(height)
        se.annotation.set(text=height,
                           position=(0, 20), anncoords="offset points")
        se.annotation.xy = (x + width / 2, y + height)

    colors = {'west': 'blue', 'southwest': 'black', 'midwest': 'red', 'southeast': 'yellow', 'northeast': 'green'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)

    plt.show()

def futureFireGraph10Year(w, sw, mw, se, ne):
    data = [sum(w), sum(sw), sum(mw), sum(se), sum(ne)]
    data = np.array(data).flatten()
    X = np.arange(1)
    fig, ax = plt.subplots()

    ax.bar(X + 0.1, data[0], color='b', width=0.2)
    ax.bar(X + 0.3, data[1], color='k', width=0.2)
    ax.bar(X + 0.4, data[2], color='r', width=0.2)
    ax.bar(X + 0.5, data[3], color='y', width=0.2)
    ax.bar(X + 0.6, data[4], color='g', width=0.2)

    ax.set_xticks([0, 0.7])
    ax.set_xticklabels(['2022', '2032'])
    ax.set_ylabel('Fire Outbreak Count')
    ax.set_xlabel('Years')
    ax.set_title('Predicted Fire Outbreak Next 10 Years')

    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)
    @cursor.connect("add")
    def on_add(se):
        x, y, width, height = se.artist[se.target.index].get_bbox().bounds
        height = round(height)
        se.annotation.set(text=height,
                           position=(0, 20), anncoords="offset points")
        se.annotation.xy = (x + width / 2, y + height)

    colors = {'west': 'blue', 'southwest': 'black', 'midwest': 'red', 'southeast': 'yellow', 'northeast': 'green'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)

    plt.show()

def futureFireGraph15Year(w, sw, mw, se, ne):
    data = [sum(w), sum(sw), sum(mw), sum(se), sum(ne)]
    data = np.array(data).flatten()
    X = np.arange(1)
    fig, ax = plt.subplots()

    ax.bar(X + 0.1, data[0], color='b', width=0.2)
    ax.bar(X + 0.3, data[1], color='k', width=0.2)
    ax.bar(X + 0.4, data[2], color='r', width=0.2)
    ax.bar(X + 0.5, data[3], color='y', width=0.2)
    ax.bar(X + 0.6, data[4], color='g', width=0.2)

    ax.set_xticks([0, 0.7])
    ax.set_xticklabels(['2022', '2037'])
    ax.set_ylabel('Fire Outbreak Count')
    ax.set_xlabel('Years')
    ax.set_title('Predicted Fire Outbreak Next 15 Years')

    cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)
    @cursor.connect("add")
    def on_add(se):
        x, y, width, height = se.artist[se.target.index].get_bbox().bounds
        height = round(height)
        se.annotation.set(text=height,
                           position=(0, 20), anncoords="offset points")
        se.annotation.xy = (x + width / 2, y + height)
    colors = {'west': 'blue', 'southwest': 'black', 'midwest': 'red', 'southeast': 'yellow', 'northeast': 'green'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)

    plt.show()

if __name__ == '__main__':
    readDataIntoHistogram()