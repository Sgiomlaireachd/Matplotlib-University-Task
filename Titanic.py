import matplotlib.pyplot as plt

class Passanger:
    def __init__(self,args):
        self.pclass = args[0]
        self.survived = args[1]
        self.name = args[2]
        self.sex = args[3]
        self.age = args[4]
        self.sibsb = args[5]
        self.parch = args[6]
        self.ticket = args[7]
        self.fare = args[8]
        self.cabin = args[9]
        self.embarked = args[10]
        self.boat = args[11]
        self.body = args[12]
        self.home_dest = args[13]
def graphs(passangers):
    # Amount of survivalists
    variants = ['Survived','Died']
    psngrs = [0,0]
    for i in passangers:
        if int(i.survived):
            psngrs[0] += 1
        else:
            psngrs[1] += 1
    plt.bar(variants,psngrs)
    plt.title("Survived or not")
    # plt.show()
    # Survive by classes
    classes = ['1','2','3']
    psngrs = [0,0,0]
    for i in passangers:
        if int(i.pclass) == 1:
            psngrs[0] += 1
        elif int(i.pclass) == 2:
            psngrs[1] += 1
        else:
            psngrs[2] += 1
    plt.bar(classes,psngrs)
    plt.title("Survived depends on classes")
    # plt.show()
    # Survived by age
    ages = set([float(i.age) for i in passangers if i.age != ''])
    print(ages)
    survived = []
    for i in ages:
        count = 0
        for j in passangers:
            print(j.name)
            if float(j.age) == i:
                count += int(j.survived)
        survived.append(count)
    print(ages)
    print(survived)

    


passangers = []
with open('/home/denis/Desktop/Python/Goshko/titanic.csv') as file:
    for line in file:
        while '"' in line: line = line.replace('"', ' ')
        line = line.split(',')
        del line[3]
        passangers.append(Passanger(line))
graphs(passangers)