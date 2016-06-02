"""Car module for the hit text based adventure
Car Adventure"""

import random

EVENTS = [
    "gas_station",
    "nothing",
    "nothing",
    "nothing",
    "nothing",
    "nothing"]
BOOL = [
    True,
    False]
random.shuffle(EVENTS)

class Car():
    """Your car."""

    def __init__(self, make, model, year, fuel_capacity, color=None, at_gas_station = False, at_bank = False, money=100):
        """Atributtes of your car, fuel in gallons."""
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.money = money
        self.fuel_capacity = fuel_capacity
        self.fuel_level = self.fuel_capacity
        self.at_gas_station = at_gas_station
        self.at_bank = at_bank
        if self.year < 2000:
            print("Your car is old")
            
    def refuel(self):
        """Fill up your gas."""
                
        if self.fuel_level >= self.fuel_capacity:
            print("Your tank is already full :P")
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == False:
            print("You are not at a gas station and therfore can't fill up") 
        elif self.fuel_level < self.fuel_capacity and self.at_gas_station == True:
            for i in range(self.fuel_level, self.fuel_capacity):
                self.money = self.money -2
            print("Your fuel tank has been filled")
            self.fuel_level = self.fuel_capacity

    def drive(self):
        """Drive your car"""
        self.fuel_level = self.fuel_level -1
        
        if self.fuel_level > 1:
            print("Your car is moving")
            
        if self.fuel_level <= self.fuel_capacity /2 and self.fuel_level > 0:
            print(self.fuel_level -1)
        
        if self.fuel_level <= 1:
            print("You need more gas")
        elif random.choice(EVENTS) == "gas_station":
            self.at_gas_station = True
            print("You are at a gas station")
        elif random.choice(EVENTS) == "bank":
            self.at_bank = True
            print("You are at a bank")
        elif random.choice(EVENTS) != "gas_station":
            self.at_gas_station = False
        elif random.choice(EVENTS) != "bank":
            self.at_bank = False

    def specs(self):
        """Display specs of your car"""
        print(self.color, self.year, self.make, self.model,
        self.fuel_capacity, "Gallons", self.money, "moneys")
        
def loot(self):
        if self.at_bank == True:
            if random.choice(BOOL) == False and self.at_bank == True:
                print("No money here")
            elif random.choice(BOOL) == True and self.at_bank == True:
                self.money = self.money + random.randrange(1,50)
                print("You found some money you now have", self.money)
        elif random.choice(EVENTS) != "bank":
            self.at_bank = False
            print("you are not at a bank and therefore there is nothing to loot")
