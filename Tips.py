import matplotlib.pyplot as plt

class Tip:
    def __init__(self,args):
        self.total_bill = args[0]
        self.tip = args[1]
        self.sex = args[2]
        self.smoker=args[3]
        self.day = args[4]
        self.time=args[5]
        self.size=args[6]
        self.fraction=args[7]
    def __repr__(self):
        return '{} | {} | {} | {} | {} | {} | {} | {}'.format(self.total_bill,self.tip,self.sex,self.smoker,self.day,self.time,self.size,self.fraction)
def whoGivesMoreTips(tips):
    avg_smokers,avg,cs,c = 0,0,0,0
    for i in tips:
        if i.smoker == "Yes":
            avg_smokers += float(i.tip)
            cs+=1
        if i.smoker == "No":
            avg += float(i.tip)
            c+=1
    if avg_smokers/cs > avg/c:
        print("RESULT: Smokers tip more.")
    else:
        print("RESULT: Non-smokers tip more.")
def tipsInDays(tips):
    bin = ['Sun','Mon','Tue','Wed','Thur','Fri','Sat']
    days = [i.day for i in tips]
    tip = [days.count('Sun'),days.count('Mon'),days.count('Tue'),days.count('Wed'),days.count('Thur'),days.count('Fri'),days.count('Sat')]
    plt.bar(bin,tip)
    plt.title("Tips in days of a week")
    plt.show()
def tipsInDaytimes(tips):
    bin = ['Dinner','Lunch']
    times = [i.time for i in tips]
    tip = [times.count("Dinner"),times.count("Lunch")]
    plt.bar(bin,tip,label="Tips")
    plt.title("Tips in daytimes")
    plt.show()
def scatter(tips):
    bill = [float(i.total_bill) for i in tips]
    tip = [float(i.tip) for i in tips]
    plt.scatter(bill,tip)
    plt.title("Scatter bill-tip")
    plt.show()
def dependencyTipOnSex(tips):
    bin = ["Male","Female"]
    sexes = [i.sex for i in tips]
    tip = [sexes.count("Male"),sexes.count("Female")]
    plt.bar(bin,tip)
    plt.title("Dependency of tip and sex")
    plt.show()
tips = []
with open('/home/denis/Desktop/Python/Goshko/tips.csv') as file:
    for line in file:
        tips.append(Tip(line.split(',')))
whoGivesMoreTips(tips)
tipsInDays(tips)
tipsInDaytimes(tips)
scatter(tips)
dependencyTipOnSex(tips)