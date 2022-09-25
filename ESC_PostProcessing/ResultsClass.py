from curses import get_escdelay


class ResultsClass(object):

    #class variables
    Teamname = ""
    Carname = ""
    Carclass = ""
    FastestSpeedKMH = None
    FastestLap = None
    NumberOfLaps = None
    NumberOfPits = None
    Laptimes = None
    Pitstops = None
    Stintlength = None
    averageLapTime = None

    def __init__(self, Teamname, Carname, Carclass, FastestSpeedKMH, FastestLap, NumberOfLaps, NumberOfPits, Laptimes, Pitstops, Stintlength):
        self.Teamname = Teamname
        self.Carname = Carname
        self.Carclass = Carclass
        self.FastestLap = FastestLap
        self.FastestSpeedKMH = FastestSpeedKMH
        self.NumberOfLaps = NumberOfLaps
        self.NumberOfPits = NumberOfPits
        self.Laptimes = Laptimes
        self.Pitstops = Pitstops
        self.Stintlength = Stintlength

    def get_sec(self, time_str):
        n = time_str.count(":")
        if (n > 2):
            print("Error handling the timestring")
        if (n == 2):
            h, m, s = time_str.split(':')
            return int(h) * 3600 + int(m) * 60 + float(s)
        if (n == 1):
            m, s = time_str.split(':')
            return int(m) * 60 + float(s)

    def CalcAverageLapTime(self):
        # sum up all lap times
        total = 0
        for i in self.Laptimes:
            total += self.get_sec(i)
        if(self.NumberOfLaps != 0):
            self.averageLapTime = total / self.NumberOfLaps
        else: self.averageLapTime = 0
        return


