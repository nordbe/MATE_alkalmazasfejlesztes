# Vizsga projekt - Biró László Norbert NK: A19AE6

## Projekt rövid ismertetetése

A vizsgaprojekt céla egy Python-ban elkészített játék, a 2048, elkésztíése tkinter csomag felhasználásával. A felhasználó a grafikus felületen a nyílbillentyűk segítéségével  képes a pályán lévő (4x4 mátrix) számokat mozgatni. 
A pontok záma mindig az összevont mezők pontértékével növekszik. Az egymás mellett lévő ugyanakkora számok minden mozgatás, tolás során összeolvadnak, összeadódnak és így lesznek egyre nagyobb értékűek. A játék célja, hogy össze tudjunk hozni egy 2048 értékű mezőt, de persze a játék itt nem ér véget, további cél lehet a 4096, vagy akár a 8192 értékű mező kirakása.

## Projekt technikai részletei:
**Programozási nyelv:** Python

**Fejlesztői környezet:** PyCharm GitHub integrációval

**Github repo**: [https://github.com/nordbe/MATE_alkalmazasfejlesztes](https://github.com/nordbe/MATE_alkalmazasfejlesztes)

**Használt csomagok:** 
- tkinter
- random

### Funkcionális leírás

#### Általános működés:

- Indítás után garfikus ablak jelenik meg.
- Az ablak címsorában a játék- és a készítő neve és NEPTUN kódja jelenik meg
- A menüsorban egy **gomb** segítségével lehet új játékot indítani
- A gomb mellett kiírásra kerül az adott játékmenetben elért pontszám, illetve a legmagasabb elért pontszám
- A játékterület egy 4*4 rács, egy-egy cella/mező egy mozgatható területet jelöl, amelyek a **lefele, felfele, jobbra, és balra** nyilakkal mozgathatóak.
- A cellákban számok szerepelnek, amelyek értékei 2,4,8,16,32...2048 lehetnek.
- Az egyes mezők attól függően, hogy milyen értéket vesznek fel eltérő háttér- és betűszínnel rendelkeznek.
- A játék bezárható, teljes képernyőre tehető, illetve minimalizáható az ablak címsorának jobb oldalán megjelenő funkció gombokkal.
- A játék véget ér:
  - Ha nincs már üres mező ÉS
  - Nincs további egyesíthető cella függőleges vagy vízszintes irányba VAGY
  - Bármelyik celle értéke eléri a 2048-as értéket.

#### Mozgatási szabályok
- A cella csak akkor mozgatható:
  - Ha a mozgatni kívánt irányban üres cella van
  - A mozgás során a cellák nem ugranak át más cellákon
  - Csak a játétéren belül mozoghat
- A mozgás iránya:
  - Fel - minden cella a lehető legtávolabbra mozdul felfelé
  - Le - minden cella a lehető legtávolabbra mozdul lefele
  - Bal - minden cella a lehető legtávolabbra mozdul balra
  - Jobb - minden celle a lehető legtávolabbra mozdul jobbra

#### Egyesítési szabályok
- Egyesítési szabályok:
  - Azonos értékű cellák egyesülhetnek ÉS
  - Egymás mellett vannak a mozgás irányában ÉS
  - Nincs más cella köztük ÉS
  - Minden mozgás során legfeljebb egyszer egyesülhet egy cella
- Egyesítés során a cellák érékei összeadódnak és az lesz az új mező értéke
- Minden sikeres mozgatás után új mező jelenik meg a játéktérben:
  - Az új cella értéke 2 vagy 4 lehet
  - A megjelenés helye véletlenszerűen kerül kiválasztásra az üres mezők közül
- Speciális esetek
  - Többszörös egyesítés:  
    - `balra mozgatás [2,2,2,2] » [4,4,0,0]`
    - az első 2-es egyesül 4-essé
    - a második 2-es egyesül 4-essé
    - nem jön létre 8-as, mert csak egyszer egyesülhet egy cella egy mozgás során
  - Prioritás:
    - `balra mozgatás [2,2,4,4] » [4,8,0,0]`
  - Blokkoló mezők:
    - `balra mozgatás [2,4,2,0] » [2,4,2,0]`
    - nincs változás, mert egyik cella sem tud mozogni

