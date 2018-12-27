import matplotlib.pyplot as plt
class Airport:
    def __init__(self, args):
        self.CarrierCode = args[0]
        self.Date = args[1]
        self.FlightNumber = args[2]
        self.TailNumber = args[3]
        self.DestinationAirport = args[4]
        self.ScheduledDepartureTime = args[5]
        self.ActualDepartureTime = args[6]
        self.ScheduledElapsedTime = args[7]
        self.ActualElapsedTime = args[8]
        self.DepartureDelay = args[9]
        self.WheelsOffTime = args[10]
        self.Taxi_out = args[11]
    def __repr__(self):
        return "{} | {} | {} | {} | {} | {}".format(self.CarrierCode,self.Date,self.FlightNumber,self.TailNumber,self.DestinationAirport,self.Taxi_out)

def dependencyDelayFromElapseTime(flights):
    delays = [int(i.DepartureDelay) for i in flights]
    delays = sorted(delays)
    elapsetimes = [int(i.ActualElapsedTime) for i in flights]
    elapsetimes = sorted(elapsetimes)
    plt.plot(delays,elapsetimes)
    plt.xlabel("Delays")
    plt.ylabel("Elapsed Time")
    plt.title("Dependency of delays and elapsed time")
    plt.show()



def min_max_Tasks(flights):
    min = 0
    min1 = 0
    max1 = 0
    max = 0
    for i in flights:
        if int(i.ActualElapsedTime) > max:
            max = int(i.ActualElapsedTime)
        if int(i.ActualElapsedTime) < min:
            min = int(i.ActualElapsedTime)
        if int(i.DepartureDelay) > max1:
            max1 = int(i.DepartureDelay)
        if int(i.DepartureDelay) < min1:
            min1 = int(i.DepartureDelay)
    print("Min elapsed time:", min,"\nMax elapsed time:",max,"\nMin departuare delay:",min1,"\nMax departure delay:",max1)
def numberOfFlights(flights):
    print("How many times each plane flew:")
    planes = set()
    count = 1
    for i in flights:
        planes.add(i.TailNumber)
    for i in planes:
        c = 0
        for j in flights:
            if j.TailNumber == i:
                c+=1
        if count % 7 == 0:
            symbol = "\n"
        else:
            symbol = "\t"
        print("|",i,':',c,end=symbol,sep="")
        count += 1
def averageDelayInMonth(month,flights):
    sum = 0
    for i in flights:
        if int(i.Date[0] + i.Date[1]) == month:
            sum += int(i.DepartureDelay)
    print("\nAverage delay in this month:", sum/len(flights))
def averageDelayInLocation(location,flights):
    sum = 0
    for i in flights:
        if i.DestinationAirport == location:
           sum += int(i.DepartureDelay)
    print("Average delay in {}:".format(location), sum/len(flights))
def averageDelayInDays(flights):
    print("Average delay in days:")
    for day in range(1,32):
        count = 0
        sum = 0
        for i in flights:
            if int(i.Date[3] + i.Date[4]) == day:
                sum += int(i.DepartureDelay)
                count += 1
        print("Day:",day,"|",sum/count)
def flightInDay(day,month,flights):
    print("Amount of flights in {}st day and in {}th month".format(day,month))
    destindations = set()
    for i in flights:
        destindations.add(i.DestinationAirport)
    for i in destindations:
        count = 0
        count1 = 0
        for j in flights:
            if j.DestinationAirport == i and int(j.Date[3] + j.Date[4]) == day:
                count += 1
            if j.DestinationAirport == i and int(j.Date[0] + j.Date[1]) == month:
                count1 += 1
        print(i,"|","That day:",count,", That month:",count1)
list = []
with open('airport.csv') as file:
    for line in file:
        list.append(Airport(line.split(',')))
flightInDay(1,7,list)
numberOfFlights(list)
averageDelayInMonth(7,list)
averageDelayInLocation("SAN",list)
averageDelayInDays(list)
min_max_Tasks(list)
dependencyDelayFromElapseTime(list)