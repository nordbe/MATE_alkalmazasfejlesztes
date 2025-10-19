# Vizsga projekt - Biró László Norbert NK: A19AE6

## Projekt rövid ismertetetése

A vizsgaprojekt céla egy Python-ban elkészített játék, a 2048, elkésztíése tkinter csomag felhasználásával. A felhasználó a grafikus felületen a nyílbillentyűk segítéségével  képes a pályán lévő (4x4 mátrix) számokat mozgatni. 
A pontok záma mindig az összevont mezők pontértékével növekszik. Az egymás mellett lévő ugyanakkora számok minden mozgatás, tolás során összeolvadnak, összeadódnak és így lesznek egyre nagyobb értékűek. A játék célja, hogy össze tudjunk hozni egy 2048 értékű mezőt, de persze a játék itt nem ér véget, további cél lehet a 4096, vagy akár a 8192 értékű mező kirakása.

## Projekt technikai részletei:
**Programozási nyelv:** Python

**Fejlesztői környezet:** PyCharm GitHub integrációval

**Github repo**: [https://github.com/nordbe/MATE_alkalmazasfejlesztes](https://github.com/nordbe/MATE_alkalmazasfejlesztes)

**Használt csomagok:** 
- math
- random
- pygame

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

## Fejlesztési dokumentáció
***2025.10.12***

- Szükséges modulok importálása: `random` `pygame` `math`
- UI-hoz szükséges változók/konstanstok létrehozása (méret, szín, betűtípus)
- Játék ablak futtasához szükséges alapkódok megírása
- `draw()` függvény megírása (háttér frissítése), `main()` függvény frissítése
- `draw_grid()` függvény megírása rács létrehozásához

***2025.10.13***

- `Tile(csempe)` osztály definiálása:
  - `COLORS`: lista, amely tuplek-ben tartalmazza a színkódokat
  - konstruktor létrehozása
  - `get_color()` függvény:  csempe színék meghatározása a `COLORS` listából. Index lekérésée logartimus használata, mert:
    - 2 érték esetén » 0. index
    - 4 érték esetén » 1. index
    - 8 érték esetén » 3. index
    - 16 érték esetén » 4. index
    - 
  - `draw()` függvény: kirajzolja a rács megfelelő cellájába a csempét, majd annak értékét elhelyezi a közepére
  - `move()` függvény: 
  - `set_pos()` függvény:
- `draw()` függvény frissítése, paraméterlista bővítése csempe rajzolásával
- `main()`függvény bővítése csempe kirajzolására

***2025.10.17***

- `generate_tiles()` függvény elkészítése a csempék legenáráláshoz, tuple-t használok (`tiles ={}`)
- `get_rand_pos()` függvény elkészítése, és a `generate_tiles()` függvény frissítése
- `main()` függvény frissítése.

***2025.10.17***
- Csempék mozgatásának alogoritmizálása, elvi működés kitalálása
  - Lehetséges alapesetek lemodellezése: 
    - V1: X1Y2 Cella értéke 2, mozgás balra üres cella » OK
    - V2: X1Y2 Cella értéke 2, X0Y2 értéke: 4 » NOK
    - V3: X1Y2 Cella értéke 2, X0Y2 értéke: 2 » OK » X0Y2 cella értékének növelése, X1Y2 cella "törlése "
    - etc..
  - Lehetséges összetett esetek lemodellezése:
    - Egymés melletti cellákban lévő nem üres csempék kezelése
    - Precedencia sorrend meghatározása a mozgásnál
- `move_tiles()` függvény megírása, amely felel  a csempék mozgatásáért
  - `if/elseif` feltételben használt változók, lambda függvények:
    - `sort_func`: meghatározza hogyan rendezzük a csempéket (oszlop szerint jobbra/balra, sor szerint le/fel)
    - `reverse`: megadja a rendezés irányát
    - `delta`: a csempa egy lépésben történő elmozdulásának vektora
    - `boundary_check`: ellenőrzi, hogy a pálya szélén vagyunk-e?
    - `get_next_tile`: legközelebbi csempe keresése a mozgás irányába
    - `merge_check`: Ellenőrzi, hogy a mozgó és szomszédos csempe elég közel van-e egymáshoz?
    - `move_check`: Ellenőrzi, hogy a két csempe között van-e még hely, hogy a mozgó csempe tovább haladjon
    - `ceil`: Meghatározza, hogy a csempe rácsnégyzetének kiszámításához a koordinátákat felfelé (ceil) vagy lefelé (floor) kerekítsük-e

 