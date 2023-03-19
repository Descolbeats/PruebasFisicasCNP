def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

class Tests():
    arrBarTimes = [36, 41, 46, 52, 57, 63, 70, 78, 86, 95]
    arrCircuitTimes = [12.7, 12.5, 12.3, 12, 11.6, 11.2, 10.8, 10.3, 9.8, 9.3]
    arrRaceTimes = [4 * 60 + 45, 4 * 60 + 36, 4 * 60 + 27,\
        4 * 60 + 18, 4 * 60 + 9, 4 * 60, 3 * 60 + 51,\
        3 * 60 + 42, 3 * 60 + 33, 3 * 60 + 24]
    def __init__(self):

        # Times
        self.barTime = "-"
        self.circuitTime = "-"
        self.raceTime = "-"
        self.raceTimeMin = "-"
        self.raceTimeSec = "-"

        # Intervals
        self.barInterval = "-"
        self.circuitInterval = "-"
        self.raceInterval = "-"

        # Grades
        self.barGrade = "-"
        self.circuitGrade = "-"
        self.raceGrade = "-"
        self.totalGrade30 = "-"
        self.totalGrade10 = "-"

        # Strings
        self.strRaceTime = "-"
        self.strBarGrade = "-"
        self.strCircuitGrade = "-"
        self.strRaceGrade = "-"
        self.strTotalGrade = "-"

    def set_bar_time(self, time):
        time = time.replace(",", "." )
        time = '0' if not time or not isFloat(time) else time
        self.barTime = int(float(time))
    def set_circuit_time(self, time):
        time = time.replace(",", "." )
        time = '0' if not time or not isFloat(time) else time
        self.circuitTime = int(time) if float(time).is_integer() else float(time)
    def set_race_time(self, timeMin, timeSec):
        timeMin = timeMin.replace(",", "." )
        timeSec = timeSec.replace(",", "." )
        timeMin = '0' if not timeMin or not isFloat(timeMin) else timeMin
        timeSec = '0' if not timeSec or not isFloat(timeSec) else timeSec
        self.raceTime = int(float(timeMin)) * 60 + int(float(timeSec))
        self.raceTimeMin = int(self.raceTime // 60)
        self.raceTimeSec = int(self.raceTime % 60)
        strRaceTimeMin = str(self.raceTimeMin)
        strRaceTimeSec = str(self.raceTimeSec) if self.raceTimeSec > 9 else "0" + str(self.raceTimeSec)
        self.strRaceTime = strRaceTimeMin + ":" + strRaceTimeSec
    def calc_all(self):
        self.calc_bar_grade()
        self.calc_circuit_grade()
        self.calc_race_grade()
        self.calc_total_grade()
        self.calc_bar_interval()
        self.calc_circuit_interval()
        self.calc_race_interval()
    def calc_bar_grade(self):
        self.barGrade = 0
        for i in range(len(Tests.arrBarTimes)):
            if self.barTime >= Tests.arrBarTimes[i]:
                self.barGrade = i + 1
        self.strBarGrade = str(self.barGrade) + "/10"
    def calc_circuit_grade(self):
        self.circuitGrade = 0
        for i in range(len(Tests.arrCircuitTimes)):
            if self.circuitTime <= Tests.arrCircuitTimes[i]:
                self.circuitGrade = i + 1
        self.strCircuitGrade = str(self.circuitGrade) + "/10"    
    def calc_race_grade(self):
        self.raceGrade = 0
        for i in range(len(Tests.arrRaceTimes)):
            if self.raceTime <= Tests.arrRaceTimes[i]:
                self.raceGrade = i + 1
        self.strRaceGrade = str(self.raceGrade) + "/10"
    def calc_total_grade(self):
        self.totalGrade30 = 0
        if self.barGrade != "-":
            self.totalGrade30 += self.barGrade
        if self.circuitGrade != "-":
            self.totalGrade30 += self.circuitGrade
        if self.raceGrade != "-":
            self.totalGrade30 += self.raceGrade
        self.totalGrade10 = int(self.totalGrade30/3) if self.totalGrade30%3 == 0 else round(self.totalGrade30/3, 1)
        self.strTotalGrade = str(self.totalGrade30) + "/30 (" + str(self.totalGrade10) + "/10)"



    def calc_bar_interval(self):
        if not self.barGrade:
            self.barInterval = f"[0 - {Tests.arrBarTimes[0]-1}]"
        elif self.barGrade != 10:
            self.barInterval = f"[{Tests.arrBarTimes[self.barGrade-1]} - {Tests.arrBarTimes[self.barGrade]-1}]"
        else:
            self.barInterval = f"[{Tests.arrBarTimes[9]} - Inf.]"
    def calc_circuit_interval(self):
        if not self.circuitGrade:
            self.circuitInterval = f"[{round(Tests.arrCircuitTimes[0]+0.1,1)} - Inf.]"
        elif self.circuitGrade != 10:
            self.circuitInterval = f"[{Tests.arrCircuitTimes[self.circuitGrade-1]} - {round(Tests.arrCircuitTimes[self.circuitGrade]-0.1,1)}]"
        else:
            self.circuitInterval = f"[0 - {Tests.arrCircuitTimes[9]}]"
    def calc_race_interval(self):
        if not self.raceGrade:
            self.raceInterval = f"[{Tests.arrRaceTimes[0]//60}:{Tests.arrRaceTimes[0]%60} - Inf.]"
        elif self.raceGrade != 10:
            self.raceInterval = f"[{Tests.arrRaceTimes[self.raceGrade-1]//60}:{Tests.arrRaceTimes[self.raceGrade-1]%60} - {Tests.arrRaceTimes[self.raceGrade]//60}:{Tests.arrRaceTimes[self.raceGrade]%60-1}]"
        else:
            self.raceInterval = f"[0 - {Tests.arrRaceTimes[9]//60}:{Tests.arrRaceTimes[9]%60}]"