import matplotlib.pyplot as plt
class Car:
    def __init__(self,args):
        self.mpg = args[0]
        self.cyl = args[1]
        self.displ = args[2]
        self.hp = args[3]
        self.weight = args[4]
        self.accel = args[5]
        self.yr = args[6]
        self.origin = args[7]
        self.name = args[8]
    def __repr__(self):
        return '{} | {} | {} | {} '.format(self.mpg,self.cyl,self.origin,self.name)
def graphs(cars):
    origins = list(set([i.origin for i in cars]))
    car_origins = [i.origin for i in cars]
    amounts = [car_origins.count(i) for i in origins]
    plt.bar(origins,amounts)
    plt.title("Amount of cars by origins")
    plt.show()
    ####################################################
    mpgs = sorted([float(i.mpg) for i in cars])
    names = sorted([i.name.split(' ')[0] for i in cars])
    plt.bar(names,mpgs)
    plt.title("Graph by Miles per Gallon")
    plt.show()
    ####################################################
    cyls = sorted(set([float(i.cyl) for i in cars]))
    hps = []
    for i in cyls:
        sum = 0
        count = 0
        for j in cars:
            if float(j.cyl) == i:
                sum += float(j.hp)
                count += 1
        hps.append(sum/count)
    plt.bar(cyls,hps)
    plt.title("Dependency of cylinders and horse powers")
    plt.show()
    ######################################################
    origins = list(set([i.origin for i in cars]))
    mpgs = []
    weights = []
    for i in origins:
        sum,sum1 = 0,0
        count = 0
        for j in cars:
            if j.origin == i:
                sum1 += float(j.weight)
                sum += float(j.mpg)
                count += 1
        mpgs.append(sum/count)
        weights.append(sum1/count)
    plt.bar(origins,mpgs)
    plt.title("Dependency of origin and miles per galon")
    plt.show()
    ######################################################
    plt.bar(origins,weights)
    plt.title("Average weight in different origins")
    plt.show()
    ######################################################
    years = list(set([i.yr for i in cars]))
    crs = []
    for i in years:
        count = 0
        for j in cars:
            if j.yr == i:
                count += 1
        crs.append(count)
    plt.bar(years,crs)
    plt.title("Amount of cars per year")
    plt.show()


cars = []
with open('cars.csv')  as file:
    for line in file:
        cars.append(Car(line.split(',')))
graphs(cars)