class Vehicle:
    # attribs: vehicleName, TeamName, totalLaps, lastLap, allLapsTime, allLapPits, sectorTimes[3],
    vehicleName = ""
    TeamName = ""
    totalLaps = 0
    lastLap = 0
    allLapsTime = []
    allLapPits = []
    sectorTimes = [0, 0, 0]

    def __init__(self, vName, tName):
        self.vehicleName = vName
        self.TeamName = tName

    def setTotalLaps(self, laps):
        self.totalLaps = laps

    def setAllLapsTime(self, lapTime):
        self.allLapsTime.append(lapTime)

    def setAllLapPits(self, pit):
        self.allLapPits.append(pit)

    def setSectorTimes(self, times1, times2, times3):
        self.sectorTimes[0].append(times1)
        self.sectorTimes[1].append(times2)
        self.sectorTimes[2].append(times3)

    def __str__(self) -> str:
        return f'Vehicle: {self.vehicleName}, Team: {self.TeamName}, Total Laps: {self.totalLaps}, Last Lap: {self.lastLap}, All Laps Time: {self.allLapsTime}, All Lap Pits: {self.allLapPits}, Sector Times: {self.sectorTimes}'
