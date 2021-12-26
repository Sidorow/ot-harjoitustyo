# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne on suhteellisen yksinkertainen ja se noudattaa kaksitasoista kerrosarkkitehtuuria:

(tähän uml)

## Käyttöliittymä

Sovelluksessa on kaksi eri näkymää:

- Aloitusikkuna
- Peli-ikkuna

Kumpikin ikkuna on toteutettu omana luokkanaan. UI -luokka hallitsee, kumpi ikkunoista on näkyvissä. Sovelluslogiikkaa on pyritty eristämään käyttöliittymästä mahdollisimman paljon.

## Sovelluslogiikka

Sovelluksen pääasialliset toiminnallisuudet sisältyy 'GameService' -luokkaan. Luokka hakee tiedostosta pelin tehtävät ja kiroukset alustuksen aikana. Sovelluslogiikka injektoidaan sekä aloitus- että peli-ikkunan riippuvuudeksi. Luokassa on useita listoja, joita käytetään pelin aikana, kuten pelaajalista ja tehtävälista. Kumpaakin näistä käyttäjä voi muokata käyttöliittymän kautta. Pelaajien ja tehtävien lisääminen onnistuu luokan metodeilla:

- add_players(playername)
- write_task(task)

Kummassakin metodissa annetut argumentit lisätään listaan ja write_task -metodi lisää sen lisäksi sen pysyväksi riviksi tiedostoon. 

## Pysyväistallennus

Sovellus voi tallentaa ja poistaa tekstiä tiedostosta luokan 'GameService' avulla. Tekstiä tallennetaan yksinkertaisiin tekstitiedostoihin, joista sovellus sitten lukee rivit käynnistyksen yhteydessä.

### Tiedostot

Sovellus tallettaa tehtäviä ja kirouksia kahteen tekstitiedostoon.

Kansiossa nämä tiedostot ovat seuraavat:

'tasks.txt'

'curses.txt'

Tehtävät ja kiroukset luetaan yksinkertaisesti riveittäin, jotka tallennetaan pelin ajaksi omiin listoihin.

## Päätoiminnallisuudet



### Pelaajien lisääminen



### Tehtävien/Kirousten lisääminen



### Pelin kulku
