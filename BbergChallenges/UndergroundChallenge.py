class UndergroundSystem:
    def __init__(self):
        self.check_in_dict = {}
        self.check_out_dict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_dict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_in_dict[id]
        if (startStation, stationName) in self.check_out_dict:
            self.check_out_dict[(startStation, stationName)] = (
            self.check_out_dict[(startStation, stationName)][0] + (t - startTime),
            self.check_out_dict[(startStation, stationName)][1] + 1)
        else:
            self.check_out_dict[(startStation, stationName)] = ((t - startTime), 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ave = self.check_out_dict[(startStation, endStation)][0] / self.check_out_dict[(startStation, endStation)][1]
        return ave

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)