class Building:
    def __init__(self,numberOfFloor,buildingType):
        self.numberOfFloors = numberOfFloor
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

building1 = Building(5,'factory')
building2 = Building(10, 'office')

print(building1 == building2)

