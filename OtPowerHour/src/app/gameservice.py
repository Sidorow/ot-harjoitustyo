import random
from pathlib import Path

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
        self.tasklist = []
        self.curselist = []
        self.task_file = open("tasks.txt", encoding="utf8").read().splitlines()
        self.curse_file = open("curses.txt", encoding="utf8").read().splitlines()
        self.tasks = Path(__file__).with_name("tasks.txt")
        self.write_tasks = self.tasks.open("a", encoding="utf8")
        self.curses = Path(__file__).with_name("curses.txt")
        self.write_curses = self.curses.open("a", encoding="utf8")
        self.fill_task_list()
        self.fill_curse_list()

    def fill_task_list(self):
        """Luokan luonnin yhteydessä hakee tiedostosta tehtävät ja lisää ne listaan pelin ajaksi.

        """

        file = self.task_file
        self.tasklist.clear()
        for task in file:
            if task not in self.tasklist:
                self.tasklist.append(task)

    def fill_curse_list(self):
        """Luokan luonnin yhteydessä hakee tiedostosta kiroukset ja lisää ne listaan pelin ajaksi.

        """

        file = self.curse_file
        self.curselist.clear()
        for curse in file:
            if curse not in self.curselist:
                self.curselist.append(curse)

    def task_random(self):
        """Valitsee satunnaisen tehtävän tasklist listasta.

        Returns:
            Palauttaa satunnaisesti valitun rivin tekstiä string muodossa.
        """

        task = random.choice(self.tasklist)
        return task

    def write_task(self, task):
        """Kirjoittaa tiedostoon käyttäjän määrittelemän tehtävän.

        Args:
            task: Funktiolle annettava tehtävä string -muodossa.
        """
        self.write_tasks.write(task + "\n")
        self.tasklist.append(task)

    def delete_last_task(self):
        """Poistaa tiedostosta sekä listasta viimeisen rivin ja alkion.
        Pelattavuussyistä kaikkia rivejä ei kuitenkaan voi poistaa, vaan ensimmäinen pysyy.
        """

        last_task = self.tasklist[-1]
        new_file = open("tasks.txt", "w", encoding="utf8")
        if len(self.tasklist) > 1:
            for task in self.task_file:
                if task != last_task:
                    new_file.write(task + "\n")
            self.tasklist = self.tasklist[:-1]

    def curse_random(self):
        """Toimii identtisesti yllä mainitun task_random funktion tapaisesti,
        mutta tehtävän sijasta palautetaan satunnainen kirous.

        """

        curse = random.choice(self.curselist)
        return curse

    def write_curse(self, curse):
        """Kirjoittaa tiedostoon käyttäjän määrittelemän kirouksen.

        Args:
            curse: Funktiolle annettava kirous string -muodossa.
        """

        self.write_curses.write(curse + "\n")
        self.curselist.append(curse)

    def delete_last_curse(self):
        """Poistaa tiedostosta sekä listasta viimeisen rivin ja alkion.
        Pelattavuussyistä kaikkia rivejä ei kuitenkaan voi poistaa, vaan ensimmäinen pysyy.
        """

        last_curse = self.curselist[-1]
        new_file = open("curses.txt", "w", encoding="utf8")
        if len(self.curselist) > 1:
            for curse in self.curse_file:
                if curse != last_curse:
                    new_file.write(curse + "\n")
            self.curselist = self.curselist[:-1]

    def check_players(self):
        """Tarkistaa, että pelaajia on vähintään 3,
        joka on pelin pelattavuuden kannalta pienin määrä, joka hyväksytään.

        Returns:
            Palauttaa True, jos pelaajia on vähintään 3, muulloin False.
        """

        if len(self.players) < 3:
            return False
        return True

    def add_players(self, playername):
        """Lisää uuden pelaajan listalle.

        Args:
            playername (String): Pelaajan nimi, joka lisätään listalle.
        """

        self.players.append(playername)

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
        self.task_times.clear()
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
        self.curse_times.clear()
        while minutes >= 1:
            minutes -= 5
            if minutes == 0:
                continue
            self.curse_times.append(minutes)
