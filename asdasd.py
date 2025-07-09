
import matplotlib.pyplot as plt
def vonal():
    x = [1,2,3,4,5,6,7,8,9,10] #Adat vizszintes helye
    y = [10,25,45,15,39,22,67,35,10,5]

    plt.plot(x,y,marker="o",linestyle="-",color="blue",linewidth=1)
    plt.title("Infláció alakulása")
    plt.ylabel("Infláció mértéke")
    plt.xlabel("Évek")
    plt.show()
#vonal()
def oszlop():
    kategoriak = ["kódolás","gartic phone"]
    ertekek = [0.4,1000]
    plt.bar(kategoriak,ertekek,color="orange")
    plt.title("mi a jo a python orakban")
    plt.ylabel("dolgok")
    plt.xlabel("mennyire jo")
    plt.show()
#oszlop()
def kor():
    szeletek = ["Kendej","Béla","Zéró","Csoró Máté"]
    rész = [35,25,20,0]
    szinek = ["blue","red","red","pink"]
    plt.pie(rész,labels=szeletek,colors=szinek,startangle=140,autopct="%1.1f%%")
    plt.title("Igazságos torta(Kendé-é a legtöbb).")
    plt.show()
#kor()
def szorvany():
    #scatter
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 25, 45, 15, 39, 22, 67, 35, 10, 5]
    plt.scatter(x,y,color="black",marker="o")
    plt.title("Ak recoil")
    plt.show()
#szorvany()
def csv_diagram():#hany evesen melyik evben
    import pandas as pd
    csvfajl = pd.read_csv("oscar_age_female.csv",usecols=["Year","Age"])
    csvfajl.plot(x="Year",y="Age",kind="scatter")
    plt.title("Hány évesen nyertek melyik évben.")
    plt.show()
#csv_diagram()
def hazi():
    asd = ["Ádám","Peti","Kris","Barnabás"]
    db = [3.5,2,3,1.5]
    szin = ["pink","blue","purple","aqua"]
    plt.pie(db,labels=asd,colors=szin,startangle=0,autopct="%1.1f%%")
    plt.title("Mennyi kakaos csigat kapnak")
    plt.show()
hazi()