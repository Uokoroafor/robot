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
        print(f'{self.name} attacks {other.name} - (health = {other.health}).')
        p = random.random()
        if p>other.luck:
            other.health += self.strength
            other.check_alive()
            print(f'Attack is successful! {other.name} health is {other.health}.')
        else:
            print(f'Attack unsuccessful! {other.name} health is {other.health}.')


    def is_enemy_close(self,other):
        """if the enemy is within 1 square, squared distance is less than or equal to 2"""
        return (self.position[0]-other.position[0])**2+(self.position[1]-other.position[1])**2<=2

    def check_alive(self):
        self.alive=(self.health>0)
        return self.alive

    def print_greeting(self):
        """ Prints my robot's name and id"""
        super().print_greeting()
        print(f'{self.name} is a battle robot.')


