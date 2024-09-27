import random

# CONTROLS
global work_sadness
wage = 100
global base_consumption_probability #could be seen as consumer sentiment
base_consumption_probability = 0
global maximum_viable_hours
maximum_viable_hours = 8
global cost_to_produce
cost_to_produce = 19


# WORKER-LABORER CLASS
class Person:
    def __init__(self, id):
        self.id = id
        self.cash = 100
        self.satisfaction = 100

    # actions
    def think(self, chronos):
        soulcost = chronos.enquire_workhour_soulcost(self.id)
        # spend??
        
        # work??
        work_probability = (wage - soulcost) / wage
        if work_probability < 0:
            work_probability = 0
        # Add more logic for spending and working


# FIRM CLASS
class Firm:
    def __init__(self, id):
        self.id = id
        self.cash = 1000
    def produce(self,goods):
        current_day = Timekeeper.day
        



# MARKET CLASS
class Market:
    def __init__(self):
        self.price = 21
        self.transacted_price_history = []
        self.goods_market = []

    def list_good(self, good):
        self.goods_market.append(good)
        lowest_price = float('inf')
        for product in self.goods_market:  # add listing to market
            if product.price < lowest_price:
                lowest_price = product.price
        self.price = lowest_price  # update lowest price

    def buy_good(self):
        for product in self.goods_market:
            if self.price == product.price:
                producer = product.firm
                # Add logic for transaction


# GOOD CLASS
class Good:
    def __init__(self, firm, price):
        self.price = price
        self.firm = firm


# TIMEKEEPER CLASS
class Timekeeper:
    def __init__(self):
        self.day = 0
        self.daily_hours = {}

    def tick(self):  # increment day and reset workhours
        self.day += 1
        for key in self.daily_hours.keys():
            self.daily_hours[key] = 0

    def workhour(self, person):  # adds workhour to tally and returns how satisfaction fell
        if person not in self.daily_hours:
            self.daily_hours[person] = 0
        self.daily_hours[person] += 1

    def enquire_workhour_soulcost(self, person):  # enquire sadness
        if person not in self.daily_hours:
            self.daily_hours[person] = 0
        past = self.daily_hours[person]
        sadness = wage * (past / maximum_viable_hours)
        return sadness  

# Datalogger
class datalogger:
    def __init__(self) -> None:
        pass
        
