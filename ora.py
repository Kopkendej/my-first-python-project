import csv
def pandak():
    # pandas
    import pandas as pd
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    def megnyitas():
        csvfajl = pd.read_csv('oscar_age_female.csv')
        # print(csvfajl)
        print(csvfajl.head(20))
    # megnyitas()
    def oszlop_megnyitas():
        csvfajl = pd.read_csv('oscar_age_female.csv', usecols=["Name"])
        print(csvfajl.head(10))
    # oszlop_megnyitas()
    def atlag_eletkor():
        csvfajl = pd.read_csv("oscar_age_female.csv",usecols = ["Name","Age"])
        print(csvfajl)
        szum = csvfajl["Age"].sum()
        sor = csvfajl["Age"]
        sor = len(csvfajl["Age"])
        atlag = szum/sor
        print("A nyertesek átlag életkora:",round(atlag,2))
        atlag_eletkor()

    def legidosebb():
        csvfajl = pd.read_csv("oscar_age_female.csv", usecols=["Name", "Age"])
        print(csvfajl)
        sor = csvfajl["Age"]
        max_age = max(csvfajl["Age"])
        max_age_sor = csvfajl[csvfajl["Age"] == max_age]
        print("A legidosebb nyertes:", max_age_sor.iloc[0,1])
        print(max_age_sor.iloc[0,0], "éves.")
        legidosebb()
    def fargo():
        #melyik évben kapott oscart a fargo?
        csvfajl = pd.read_csv("oscar_age_female.csv", usecols=["Year", "Movie"], skipinitialspace= True)
        fargo_sor = csvfajl[csvfajl["Movie"] == "Fargo"]
        print("A Fargo",fargo_sor.iloc[0,1] ,"nyert Oscar dijat.")

    fargo()
pandak()