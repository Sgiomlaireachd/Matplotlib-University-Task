import matplotlib.pyplot as plt
class Population:
    def __init__(self,args):
        self.CountryName = args[0]
        self.CountryCode = args[1]
        self.Year = args[2]
        self.TotalPopulation = args[3]
        self.Urbanpopulation = args[4]
def populationInYears(pops):
    years = [year for year in range(1960,1971)]
    for year in years:
        popz = [i for i in pops if int(i.Year) == year]
        popz = popz[:34]
        bins = []
        populations = []
        for i in popz:
            if int(i.Year) == year:
                bins.append(i.CountryCode)
                populations.append(float(i.TotalPopulation))
        plt.bar(bins,populations)
        plt.title("Populations {} year".format(year))
        plt.show()

def mostUrbanized(pops):
    print("20 most urbanized countries:")
    years = [1960,1980,2000,2010]
    for year in years:
        print(year,":")
        popz = [i for i in pops if int(i.Year) == year ]
        for i in range(0,len(popz) - 1):
            for j in range(0,len(popz) - 1 - i):
                if float(popz[j].Urbanpopulation) > float(popz[j+1].Urbanpopulation):
                    popz[j],popz[j+1] = popz[j+1],popz[j]
        mostUrbanized = popz[:20]
        for i in mostUrbanized:
            print("\t",i.CountryName)
def largestCountries(pops):
    countries = ["Russian Federation","Ukraine","France","Spain","Sweden","Norway","Germany","Finland","Poland","Italy"]
    populations = []
    for i in countries:
        p = []
        for j in pops:
            if j.CountryName == i:
                p.append(float(j.TotalPopulation))
        populations.append(sum(p)/len(p))
    plt.bar(countries,populations)
    plt.title("10 Largest countries of Europe")
    plt.ylabel("Population")
    plt.show()
    ####################################################
    countries = ["Brazil","Mexico","Colombia","Argentina","Peru","Venezuela_ RB"]
    populations = []
    for i in countries:
        p = []
        for j in pops:
            if j.CountryName == i:
                p.append(float(j.TotalPopulation))
        populations.append(sum(p)/len(p))
    plt.bar(countries,populations)
    plt.title("6 Largest countries of Latin America")
    plt.ylabel("Population")
    plt.show()
    ##################################################
    countries = ["Russian Federation","China","India","Kazakhstan","Saudi Arabia","Iran_ Islamic Rep.","Mongolia","Indonesia","Pakistan","Turkey"]
    populations = []
    for i in countries:
        p = []
        for j in pops:
            if j.CountryName == i:
                p.append(float(j.TotalPopulation))
        populations.append(sum(p)/len(p))
    plt.bar(countries,populations)
    plt.title("10 Largest countries of Asia")
    plt.ylabel("Population")
    plt.show()
pops = []
with open('population.csv') as file:
    for line in file:
        pops.append(Population(line.split(',')))
# populationInYears(pops)
# mostUrbanized(pops)
largestCountries(pops)