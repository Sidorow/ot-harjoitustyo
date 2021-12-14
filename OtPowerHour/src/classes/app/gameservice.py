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
        self.read_tasks = Path(__file__).with_name("tasks.txt")
        self.tasks = self.read_tasks.open("r")
        self.read_curses = Path(__file__).with_name("curses.txt")
        self.curses = self.read_curses.open("r")


    def task_random(self):
        """Valitsee satunnaisen tehtävän tasks.txt tiedostosta.

        Returns:
            Palauttaa satunnaisesti valitun rivin tekstiä string muodossa.
        """

        tasks = self.tasks.readlines()
        task = random.choice(tasks)
        return task

    def curse_random(self):
        """Toimii identtisesti yllä mainitun funktion tapaisesti, mutta tehtävän sijasta palautetaan satunnainen kirous.

        """

        curses = self.curses.readlines()
        curse = random.choice(curses)
        return curse

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

    def spread_task_times(self):
        """Hajauttaa ajat, jolloin pelin ruudulle ilmestyy tehtävät ja lisää ne listalle.

        """

        minutes = 60
        while minutes >= 1:
            minutes -= 3
            self.task_times.append(minutes)
        for minute in self.task_times:
            if minute % 5 == 0:
                self.task_times.remove(minute)

    def spread_curse_times(self):
        """Toimii samalla tavalla kuin yllä mainittu funktio.

        """

        minutes = 60
        while minutes >= 1:
            minutes -= 5
            if minutes == 0:
                continue
            self.curse_times.append(minutes)
