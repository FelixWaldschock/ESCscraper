class Vehicle:
    # attribs: vehicleName, TeamName, totalLaps, lastLap, allLapsTime, allLapPits, sectorTimes[3],

    def __init__(self, sNumber, vName, tName):
        self.startnumber = sNumber
        self.vehicleName = vName
        self.teamName = tName
        self.totalLaps = 0
        self.lastLap = 0
        self.allLapsTime = []
        self.allLapPits = []
        self.sectorTimes = [[], [], []]

    def setTotalLaps(self, laps):
        self.totalLaps = laps

    def setLastLap(self, lap):
        self.lastLap = lap

    def addToAllLapsTime(self, lapTime):
        self.allLapsTime.append(lapTime)

    def addToAllLapPits(self, pit):
        self.allLapPits.append(pit)

    def addToSectorTimes(self, times1, times2, times3):
        self.sectorTimes[0].append(times1)
        self.sectorTimes[1].append(times2)
        self.sectorTimes[2].append(times3)

    def __str__(self) -> str:
        return f'Vehicle: {self.vehicleName}, \
            Number: {self.startnumber}, \
            Team: {self.teamName}, \
            Total Laps: {self.totalLaps}, \
            Last Lap: {self.lastLap}, \
            All Laps Time: {self.allLapsTime}, \
            All Lap Pits: {self.allLapPits}, \
            Sector Times: {self.sectorTimes}'
