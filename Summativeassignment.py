#-----------------------------------------------------------------------
#OOP Assignment 
#Ryelee McCoy
#November 8 2019
#
#--------------------------Functions/Lists------------------------------


#--------------------------Actual Code----------------------------------

class Minions:
    
    def __init__(self, level, health, attack):
        self.level = level
        self.health = health
        self.attack = attack
        
    def stats(self):
        print('{} {} {}'.format(self.level, self.health, self.attack))
        
        
class Guard(Minions):
    def __init__(self, level, health, attack, defence):
        super().__init__(level, health, attack)
        self.defence = defence
            
    def stats(self):
        print('{} {} {} {}'.format(self.level, self.health, self.attack, self.defence))

class Boss(Minions):
    def __init__(self, level, health, attack, defence, shield):
        super().__init__(level, health, attack)
        self.defence = defence
        self.shield = shield
        
    def stats(self):
        print('{} {} {} {} {}'.format(self.level, self.health, self.attack, self.defence, self.shield))

#MINION CLASS
Gremlin = Minions(1, 100, 15)
Brute = Minions(5, 200, 50)
#GUARD CLASS
BossGuard = Guard(10, 500, 75, 125)
AttackerGuard = Guard(12, 400, 150, 75)
#BOSS CLASS
Reaper = Boss(25, 1000, 300, 200, 500)

Gremlin.stats()
Brute.stats()
BossGuard.stats()
AttackerGuard.stats()
Reaper.stats()

#OOP uses classes to do all of its work for it with inheritance but procedural
#coding will be a lot more complicated to make certain classes.
#There would be a lot of more lines of code because I would need a long function
#for each class and a function for each function in each class then functions
#for the stats.
#Benefits for OOP it is a lot simpler and doesn't take up a lot of space in the 
#code
#The drawbacks of OOP is it is very difficult to learn in the first place but
#once you learn it, it makes everything easier.