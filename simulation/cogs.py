import random

# CONTROLS
global work_sadness
wage = 100
global base_consumption_probability #could be seen as consumer sentiment
base_consumption_probability = 0
global maximum_viable_hours
maximum_viable_hours = 8


# WORKER-LABORER CLASS
class person:
    def __init__(self,id):
        id=id
        cash = 100
        satisfaction = 100
    # actions
    def think(self):
        soulcost = chronos.enquire_workhour(self.id)
        wage = wage
        # spend??
        
        # work??
        work_probability = (wage - soulcost)/wage
        if work_probability<0:
            work_probability = 0

        
# FIRM CLASS
class firm:
    def __init__(self) -> None:
        vacancies = 0
        asset_value = self.get_assets(self)

    # actions
    def hire(self,person):
        pass
    # statics
    @staticmethod
    def get_assets(self):
        x = 0

# Market class
class market:
    def __init__(self) -> None:
        price = 20
        price_history = []
    def quote(self):
        return self.price
    def cash2good(self):
        

# Timekeeper
class chronos:
    def __init__(self) -> None:
        day = 0
        daily_hours = {}

    def tick(self): # increment day and reset workhours
        self.day = self.day + 1
        datalogger.tick
        for key in self.daily_hours.keys():
            self.daily_hours[key] = 0
        
    def workhour(self,person): # adds workhour to tally and returns how satisfaction fell
        self.daily_hours[person]+=1

    def enquire_workhour(self,person): # enquire sadness
        if person not in self.daily_hours.keys():
            self.daily_hours[person] = 0
        past = self.daily_hours[person]
        sadness = wage*(past/maximum_viable_hours)
        return sadness
    
# Datalogger
class datalogger:
    def __init__(self) -> None:
        pass
        
