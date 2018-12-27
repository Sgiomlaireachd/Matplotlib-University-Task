import matplotlib.pyplot as plt
import inspect
class Bachelor:
    def __init__(self,args):
        self.Year = args[0]
        self.Agriculture= args[1]
        self.Architecture= args[2]
        self.ArtandPerformance= args[3]
        self.Biology= args[4]
        self.Business= args[5]
        self.CommunicationsandJournalism= args[6]
        self.ComputerScience= args[7]
        self.Education= args[8]
        self.Engineering= args[9]
        self.English= args[10]
        self.ForeignLanguages= args[11]
        self.HealthProfessions= args[12]
        self.MathandStatistics= args[13]
        self.PhysicalSciences= args[14]
        self.Psychology= args[15]
        self.PublicAdministration= args[16]
        self.SocialSciencesandHistory= args[17]
    def getProperties(self):
        return [self.Agriculture,self.Architecture,self.ArtandPerformance,self.Biology,self.Business,self.CommunicationsandJournalism,
                self.ComputerScience,self.Education,self.Engineering,self.English,self.ForeignLanguages,self.HealthProfessions,
                self.MathandStatistics,self.PhysicalSciences,self.Psychology,self.PublicAdministration,self.SocialSciencesandHistory]
    def getPropertyNames(self):
        return ["Agriculture","Architecture","ArtandPerformance","Biology","Business","CommunicationsandJournalism",
                "ComputerScience","Education","Engineering","English","ForeignLanguages","HealthProfessions",
                "MathandStatistics","PhysicalSciences","Psychology","PublicAdministration","SocialSciencesandHistory"]
def yearsPlots(bachelors):
    years = [1975,1985,1995,2005,2010]
    percent1,percent2,percent3 = [],[],[]
    for year in years:
        for i in bachelors:
            if int(i.Year) == year:
                percent2.append(float(i.ComputerScience))
                percent1.append(float(i.Architecture))
                percent3.append(float(i.HealthProfessions))
    plt.plot(years,percent1,label="Architecture")
    plt.plot(years, percent2, label="Computer Science")
    plt.plot(years, percent3, label="Health Proffesions")
    plt.legend()
    plt.title("How women graduation changes through years")
    plt.show()
def leastAndMostFeminine(bachelors):
    print("Least and most feminine proffesions:")
    years = [1970,1980,1990,2005,2010]
    for year in years:
        for i in bachelors:
            if int(i.Year) == year:
                percents = [float(j) for j in i.getProperties()]
                Max = max(percents)
                Min = min(percents)
                M_index = percents.index(Max)
                m_index = percents.index(Min)
                print(year,"| Least feminine:",Min,i.getPropertyNames()[m_index],"|Most feminine:",Max,i.getPropertyNames()[M_index])
bachelors = []
with open("percent.csv") as file:
    for line in file:
        bachelors.append(Bachelor(line.split(',')))
yearsPlots(bachelors)
leastAndMostFeminine(bachelors)