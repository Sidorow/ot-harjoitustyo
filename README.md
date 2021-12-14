# PowerHour

Sovellus on eräänlainen juomapeli, jonka inspiraatioina on toiminut tunnettu powerhour (myös tunnettu nimellä 21) sekä hitler -juomapeli. Sovellus sekoittaa molempien pelien sääntöjä keskenään ja pyrkii tuomaan esille näiden kahden välimaaston. Lopputuloksena on sovellus, jossa on kiinteä peliaika ja joka tietyin aikavälein heittää näytölle tehtäviä tai kirouksia. Sovellus toimii parhaiten 3-9 ihmisen joukolla.

## Asennus

1. Ensimmäiseksi riippuvuudet voidaan asentaa komentorivin komennolla:

	- poetry install

2. Tämän jälkeen suoritetaan alustustoimenpiteet komennolla:

	- poetry run invoke build

3. Nyt sovellus voidaan käynnistää komennolla:

	- poetry run invoke start

## Komentorivitoiminnot

### Suoritus

poetry run invoke start

### Testaus

poetry run invoke test

### Testikattavuus

poetry run invoke coverage-report

### Pylint

poetry run invoke lint

## Dokumentaatio

[Tuntikirjanpito](https://github.com/Sidorow/ot-harjoitustyo/blob/master/OtPowerHour/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/Sidorow/ot-harjoitustyo/blob/master/OtPowerHour/dokumentaatio/vaatimusmaarittelu.md)

[Arkkitehtuurikuvaus](https://github.com/Sidorow/ot-harjoitustyo/blob/master/OtPowerHour/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/Sidorow/ot-harjoitustyo/blob/master/OtPowerHour/dokumentaatio/kayttoohje.md)

[Release](https://github.com/Sidorow/ot-harjoitustyo/releases/tag/Viikko6)
