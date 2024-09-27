# Controls
global work_sadness
wage = 100
global base_consumption_probability #could be seen as consumer sentiment
base_consumption_probability = 0
global maximum_viable_hours
maximum_viable_hours = 8
global cost_to_produce
cost_to_produce = 19
global time_to_produce
time_to_produce = 7

# Person
'''
Attributes
1. id
2. cash
3. satisfaction

Methods
1. think
2. buy
3. work
'''
class Person:
    def __init__(self, id):
        self.id = id
        self.cash = 100
        self.satisfaction = 100
    def think():
        # add logic for consumer's mind here
        pass
    def buy(self,market):
        market.buy(self)


# Firm
'''
Attributes
1. id
2. cash
3. stockpile

Methods
1. think
2. produce
3. list on market
4. change price of good on market
'''
class Firm:
    def __init__(self, id):
        self.id = id
        self.cash = 1000
        self.stockpile = []
    def think(self):
        # add logic here
        pass
    def produce(self,timekeeper):
        current_day = timekeeper.day
        deadline = time_to_produce + current_day
        timekeeper.production_orders[deadline].append(Good(self.id))

# Market
'''
Attributes
1. price
2. transacted_price_history[]
3. goods_market = []

Methods
1. list_good
2. buy_good
'''
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

    def buy_good(self,person):
        for product in self.goods_market:
            if self.price == product.price:
                price = self.price
                producer = product.firm
                person.cash-=price
                producer.cash+=price
                return True
# GOOD CLASS
'''
Attributes:
1. price
2. producer
'''
class Good:
    def __init__(self, firmid):
        self.id
        self.price = None
        self.firmid = firmid

# Timekeeper
'''
FOR STUFF THAT NEED TO CHANGE DAILY
Attributes:
1. day
2. daily_hours

Methods:
1. tick
2. workhour
3. enquire_workhour
'''
class Timekeeper:
    def __init__(self):
        self.day = 0
        self.daily_hours = {}

    def tick(self,population):   
        self.day += 1 # increment day
        for key in self.daily_hours.keys(): # reset workhours
            self.daily_hours[key] = 0


    def workhour(self, personid):  # adds workhour to tally and returns how satisfaction fell
        if personid not in self.daily_hours:
            self.daily_hours[personid] = 0
        self.daily_hours[personid] += 1

    def enquire_workhour_soulcost(self, personid):  # enquire sadness
        if personid not in self.daily_hours.items():
            self.daily_hours[personid] = 0
        past = self.daily_hours[personid]
        sadness = wage * (past / maximum_viable_hours)
        return sadness 

class Population:
    def __init__(self) -> None:
        firms = []
        persons =[]

def asset_transfer(asset,origin,target):
    for obj in origin:
        if type(asset) != type(obj):
            raise Exception('object or asset mismatch, check asset transfer list')
        if asset.id == obj.id:
            origin.remove(obj)
            target.add(obj)