from robot import Robot
import random

class BattleRobot(Robot):
    def __init__(self, identifier, name, position, direction, health=100, strength = 5, luck=0.5):
        super().__init__(identifier, name, position, direction)
        self.health = health
        self.strength = strength
        self.luck = luck
        self.alive= True

    def attack(self, other):
        p = random.random()
        if p>other.luck:
            other.health += self.strength
            other.check_alive()

    def check_alive(self):
        self.alive=(self.health>0)

    def print_greeting(self):
        """ Prints my robot's name and id"""
        super().print_greeting()
        print(f'{self.name} is a battle robot.')


