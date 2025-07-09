import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def opencsv():
    csvfile = open(r"C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv")
    data = csv.reader(csvfile, skipinitialspace=True)
    for row in data:
        print(', '.join(row))
    csvfile.close()


opencsv()

def openstable():
    pd.set_option("display.max_rows",None)
    csvfile = pd.read_csv(r"C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv",skipinitialspace=True,index_col="Year")
    print(csvfile)

openstable()

def pickcolumns(col):
    pd.set_option("display.max_rows",None)
    csvfile = pd.read_csv(r"C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv",skipinitialspace=True,usecols=col)
    print(csvfile)

pickcolumns(["Score","Title"])

def columnnames():
    csvfile = pd.read_csv("C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv",skipinitialspace=True)
    list_of_names = list(csvfile.columns)
    print("The names of the columns:",list_of_names)
columnnames()
def bestmovie():
    csvfile = pd.read_csv("C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv",skipinitialspace=True,usecols=["Score","Title"])
    max_score = max(csvfile["Score"])
    myrow = csvfile[csvfile["Score"] == max_score]
    print("The worst movie is : "+ str(myrow.iloc[0,1])+ " and its score was", str(myrow.iloc[0,0]))
bestmovie()
def worstmovie():
    csvfile = pd.read_csv("C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv",skipinitialspace=True,usecols=["Year","Score"])
    min_score = min(csvfile["Score"])
    myrow = csvfile[csvfile["Score"] == min_score]
    print("The worst movie is made in: "+ str(myrow.iloc[0,0])+ " and its score was", str(myrow.iloc[0,1]))
worstmovie()
def averagescore():
    csvfile = pd.read_csv("C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv", skipinitialspace=True,usecols=["Score"])
    avg = 0
    for i in csvfile["Score"]:
        avg += i
    avg /= len(csvfile["Score"])
    print("The average score was",round(avg,3))
averagescore()
def plotdata():
    csvfile = pd.read_csv(r"C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv", skipinitialspace=True,usecols=["Year","Score"])
    csvfile.plot(x="Year",y="Score",kind='scatter')
    plt.title("Year-Score graph")
    plt.show()
plotdata()
def plotdatacurve():
    csvfile = pd.read_csv(r"C:/Users/kopha/PycharmProjects/pythonProject/lg/deniro (1).csv",skipinitialspace=True,usecoles=["Year","Score"])
    x = np.array(csvfile["Year"])
    y = np.array(csvfile["Score"])
    coefficients = np.polyfit(x,y,3)
    poly = np.poly1d(coefficients)
    new_x = np.linspace(x[0],x[-1])
    new_y = poly(new_x)
    plt.plot(x,y,"o",new_x,new_y)
    plt.xlim([x[0] - 1,x[-1] + 1])
    plt.title("Year-Score graph")
    plt.savefig("myPlot.jpg")
    plt.show()
plotdatacurve()
