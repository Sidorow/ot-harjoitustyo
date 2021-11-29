import random
from pathlib import Path

class Service:
    def __init__(self):
        self.players = []
        self.read_tasks = Path(__file__).with_name("tasks.txt")
        self.tasks = self.read_tasks.open("r")
        self.read_curses = Path(__file__).with_name("curses.txt")
        self.curses = self.read_curses.open("r")
        
        
    def task_random(self):
        tasks = self.tasks.readlines()
        task = random.choice(tasks)
        return task
        
    def curse_random(self):
        curses = self.curses.readlines()
        curse = random.choice(curses)
        return curse
    
    def check_players(self):
        if len(self.players) < 3:
            return False
        else:
            True
        
    def add_players(self, player):
        self.players.append(player)
        
    def drink_select(self):
        player_amount = round(0.3 *len(self.players))
        players = random.sample(self.players, player_amount)
        text = "Pelaajat ottavat juoman"
        for x in players:
            text = text[:8] + " " + x + "," + text[8:]
        return text
        
    def target(self):
        target = random.choice(self.players)
        target_text = f"Kohdepelaaja on nyt {target}"
        return target_text   
    
    def choose_(self,minutes,seconds):
        return self.drink_select