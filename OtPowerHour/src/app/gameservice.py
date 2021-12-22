import random
from pathlib import Path
from app.player import Player

class Service:
    """Sovelluksen logiikasta vastaava luokka

    Attributes:
        players: Sisältää listan johon pelaaja-oliot lisätään.
        task/curse_times: Sisältää listana ajat, jolloin sovellus näyttää tehtävän tai kirouksen.
        read_tasks/curses: Avaa tehtävät/kiroukset tekstitiedostosta.
        tasks/curses: Lukee edellisen muuttujan avulla tiedoston rivit.

    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden Service -luokan.
        """

        self.players = []
        self.task_times = []
        self.curse_times = []
        self.tasks = Path(__file__).with_name("tasks.txt")
        self.read_tasks = self.tasks.open("r")
        self.write_tasks = self.tasks.open("w")
        self.curses = Path(__file__).with_name("curses.txt")
        self.read_curses = self.curses.open("r")
        self.write_curses = self.curses.open("w")


    def task_random(self):
        """Valitsee satunnaisen tehtävän tasks.txt tiedostosta.

        Returns:
            Palauttaa satunnaisesti valitun rivin tekstiä string muodossa.
        """

        tasks = self.read_tasks.readlines()
        task = random.choice(tasks)
        return task
    
    def write_task(self, task):
        self.write_tasks.write(task)
        
    def delete_last_task(self):
        self.read_tasks.readlines().pop

    def curse_random(self):
        """Toimii identtisesti yllä mainitun funktion tapaisesti, mutta tehtävän sijasta palautetaan satunnainen kirous.

        """

        curses = self.read_curses.readlines()
        curse = random.choice(curses)
        return curse
    
    def write_curse(self, curse):
        self.write_curses.write(curse)
        
    def delete_last_curse(self):
        self.read_curses.readlines().pop

    def check_players(self):
        """Tarkistaa, että pelaajia on vähintään 3, joka on pelin pelattavuuden kannalta pienin määrä, joka hyväksytään.

        Returns:
            Palauttaa True, jos pelaajia on vähintään 3, muulloin False.
        """

        if len(self.players) < 3:
            return False
        return True

    def add_players(self, playername):
        """Lisää uuden pelaaja-olion listalle.

        Args:
            playername (String): Pelaajan nimi, joka lisätään listalle.
        """

        player = Player(playername)
        self.players.append(player)

    def drink_select(self):
        """Valitsee pelaajalistalta satunnaisen pelaajan/pelaajat, jotka juovat.

        Returns:
            Palauttaa String muodossa tekstin, joka määräytyy valitun pelaajamäärän mukaan.

        """

        player_amount = round(0.3 *len(self.players))
        if player_amount <= 1:
            players = random.choice(self.players)
            text = f"Pelaaja {players} ottaa juoman"
            return text
        players = random.sample(self.players, player_amount)
        text = "Pelaajat ottavat juoman"
        for player in players:
            text = text[:8] + " " + str(player) + "," + text[8:]
        return text

    def target(self):
        """Valitsee pelaajalistalta satunnaisen kohdepelaajan.

        Returns:
            Palauttaa satunnaisesti valitun pelaajan, joka näytetään pelissä käyttöliittymän kautta.
        """

        target = random.choice(self.players)
        return target

    def spread_task_times(self, minutes):
        """Hajauttaa ajat, jolloin pelin ruudulle ilmestyy tehtävät ja lisää ne listalle.

        """
        self.task_times.clear()
        while minutes >= 1:
            minutes -= 3
            self.task_times.append(minutes)
        for minute in self.task_times:
            if minute % 5 == 0:
                self.task_times.remove(minute)

    def spread_curse_times(self, minutes):
        """Toimii samalla tavalla kuin yllä mainittu funktio.

        """
        self.curse_times.clear()
        while minutes >= 1:
            minutes -= 5
            if minutes == 0:
                continue
            self.curse_times.append(minutes)
