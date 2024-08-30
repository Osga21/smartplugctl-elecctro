import csv

espressoTime=18 #short espresso full brew is 18s long
            
class circularlist(object): #cool ring buffer from stackOverflow
    def __init__(self, size, data = []):
        """Initialization"""
        self.index = 0
        self.size = size
        self._data = list(data)[-size:]

    def append(self, value):
        """Append an element"""
        if len(self._data) == self.size:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.size

    def __getitem__(self, key):
        """Get element by index, relative to the current index"""
        if len(self._data) == self.size:
            return(self._data[(key + self.index) % self.size])
        else:
            return(self._data[key])

    def __repr__(self):
        """Return string representation"""
        return (self._data[self.index:] + self._data[:self.index]).__repr__() + ' (' + str(len(self._data))+'/{} items)'.format(self.size)         



idleThreshold = 2 #idle threshold is 2W

pumpThreshold = [34,43]

lastState="idle"
state="idle"

powerStates=circularlist(4)isPumpOn = False
isHeating = False
powerStates.append(0) #initialize 3 values
powerStates.append(0)
powerStates.append(0)

isPumpOn=False
isHeating=False

def determineState()

with open('stress.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    brewStart = 0
    isPumpOn = False
    isHeating = False

    print("Pump threshold: " + str(max(pumpThreshold)))

    for row in csv_reader:
        currTime = float(row[0])  # Current time from CSV
        powerDraw = float(row[1])  # Power draw from CSV

        print(f'\n[{currTime}s] {powerDraw}', end='')

        lastPowerStates = [powerStates[0], powerStates[-1], powerStates[-2],powerStates[-3]]
        lastPumpState = isPumpOn
        def currentState():
            
            if min(pumpThreshold) <= min(lastPowerStates) <= max(pumpThreshold):
                isPumpOn = True
            else:
                isPumpOn = False

            if max(lastPowerStates) >= max(pumpThreshold):
                isHeating = True
            else:
                isHeating = False
            
            return [isHeating,isPumpOn]
        
        def brewMonitor():
            if not lastPumpState and isPumpOn:
                brewStart = currTime
                print(" BREW STARTED", end='')

            elif lastPumpState and not isPumpOn:
                brewStart = 0
                print(" BREW ENDED", end='')

        print(f" {isHeating} {isPumpOn}")

        # Append the current power draw to powerStates for the next iteration
        powerStates.append(powerDraw)







        
""""
        if powerDraw < idleThreshold:  #idling
            if (powerStates[0] < idleThreshold and 
                powerStates[-1] < idleThreshold and
                powerStates[-2] < idleThreshold):
                
                state="idle"


        elif min(pumpThreshold) <= powerDraw <= max(pumpThreshold): #brew started, only pump is active

            if (min(pumpThreshold) <= powerSta[86.8s] 2.752 heating + brewtes[0] <= max(pumpThreshold) and
                min(pumpThreshold) <= powerStates[-1] <= max(pumpThreshold) and
                min(pumpThreshold) <= powerStates[-2] <= max(pumpThreshold)):
                    
                    state="brewing"
                    
                    if (brewStart==0):
                        brewStart=currTime
                        print("\nBREW STARTED!")

        
        elif powerDraw>max(pumpThreshold): #heating states
            offset=min(powerStates[0],powerStates[-1],powerStates[-2])

            if min(pumpThreshold) <= offset <= max(pumpThreshold) and brewStart:
                state="heating + brew"
            else:
                state="heating"
                brewStart=0


        powerStates.append(powerDraw)

        print(" "+state)
"""



False