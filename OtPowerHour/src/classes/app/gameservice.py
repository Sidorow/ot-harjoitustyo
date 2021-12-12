import random
from app.player import Player
from pathlib import Path

class Service:
    def __init__(self):
        self.players = []
        self.task_times = []
        self.curse_times = []
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
        return True

    def add_players(self, playername):
        player = Player(playername)
        self.players.append(player)

    def drink_select(self):
        player_amount = round(0.3 *len(self.players))
        if player_amount <= 1:
            players = random.choice(self.players)
            text = f"Pelaaja {players} ottaa juoman"
            print(players)
            return text
        players = random.sample(self.players, player_amount)
        text = "Pelaajat ottavat juoman"
        for player in players:
            text = text[:8] + " " + player + "," + text[8:]
        return text

    def target(self):
        target = random.choice(self.players)
        return target
    
    def spread_task_times(self):
        minutes = 60
        while minutes >= 1:
            minutes -= 3
            self.task_times.append(minutes)
        for x in self.task_times:
            if x % 5 == 0:
                self.task_times.remove(x)
                
    def spread_curse_times(self):
        minutes = 60
        while minutes >= 1:
            minutes -= 5
            self.curse_times.append(minutes)
