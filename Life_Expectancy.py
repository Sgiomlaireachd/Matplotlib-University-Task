import matplotlib.pyplot as plt
stats = []
first = False
countries = []
with open("life.csv") as file:
    for line in file:
        years = line.split(',')
        break
    for line in file:
        countries.append(line.split(',')[0])
        stats.append(line.split(',')[1:])
years[len(years) -1] = years[len(years) -1][:4]
for i in range(len(stats)): stats[i][len(stats[i]) - 1] = stats[i][len(stats[i]) - 1].replace('\n','')
# AVERAGE IN WORLD:
life = []
for i in stats:
    l = []
    for j in i:
        if j != '':
            l.append(float(j))
        else:
            l.append(0)
    life.append(l)
averages = []
for i in range(len(years)):
    sum = 0
    for j in range(len(life)):
        sum += life[j][i]
    averages.append(sum/len(countries))
years = [int(i) for i in years]
plt.plot(years,averages)
plt.title("Average in world by years")
plt.show()
# AVERAGE IN USA:
index = [i for i in range(len(countries)) if countries[i] == "United States"][0]
stats = life[index]
plt.plot(years,stats)
plt.title("Average in USA by year")
plt.show()
#AVERAGE IN JAPAN:
index = [i for i in range(len(countries)) if countries[i] == "Japan"][0]
stats = life[index]
plt.plot(years,stats)
plt.title("Average in Japan by year")
plt.show()
#AVERAGE IN UKRAINE:
index = [i for i in range(len(countries)) if countries[i] == "Ukraine"][0]
stats = life[index]
plt.plot(years,stats)
plt.title("Average in Ukraine by year")
plt.show()
Years = [1800, 1850, 1900, 1925, 1950, 1980, 2000, 2010, 2016]
for year in Years:
    index = [i for i in range(len(years)) if years[i] == year][0]
    stats = []
    for i in life:
        stats.append(i[index])
    min = 100
    i_min = 0
    i_max = 0
    max = 0
    for i in range(len(stats)):
        if stats[i] != 0 and stats[i]< min:
            min = stats[i]
            i_min = i
        if stats[i] > max:
            max = stats[i]
            i_max = i
    print(year,"year:\n","Min:",min,"-",countries[i_min],"| Max:",max,"-",countries[i_max])