Szilágyi Szabolcs Attila (HOUCBI)
Memória játék, két "lapot" fel kell fordítani, ha megegyezik akkor a lapok felfordítva maradnak, ha különböznek akkor a lapok lefordításra kerülnek, amennyiben minden lapnak a párja meg lett találva a játék gratulál a győzelmhez és kiírja, hogy hány lépésben (lap pár fordítás) sikerült megtalálni az összes párt majd kilép az alkalmazásból, a hiba elkerülése érdekében a kártyák nem aktívak az ellenőrzés alatt.
## 1. tkinter

A Tkinter Python beépített könyvtára, amely grafikus felhasználói felületek készítésére szolgál. A játék minden vizuális eleme ezzel lett megvalósítva:

Tk: Az alkalmazás főablakának létrehozására szolgál.
Button: Gombokat használunk a kártyák megjelenítéséhez.
messagebox: Felugró ablakokat hoz létre, például a játék végén a győzelem jelzésére.
grid: A gombok elrendezését segíti rácsszerű elrendezésben.

## 2. random

A Python standard könyvtárának része. A játékban a random.shuffle() függvényt használjuk, hogy véletlenszerűen rendezzük el a kártyákat a rácson, biztosítva ezzel a játék kihívását.
Osztályok és azok szerepe

## 1. SzSzAKartya

Ez az osztály egy kártyát reprezentál a játékban. A kártyáknak két állapotuk lehet: felfordított vagy lefordított.

Attribútumok:
        szoveg: A kártya tartalma (pl. 🐻 vagy 🦏).
        felforditva: Boolean érték, amely azt jelzi, hogy a kártya jelenleg felfordított állapotban van-e.

## 2. SzSzAMemoriaJatek

Ez az osztály valósítja meg a memóriajáték logikáját és a grafikus felhasználói felületet.

## Attribútumok:

        root: A Tkinter alkalmazás főablaka.
        kartyak: Egy lista, amely a játékban használt kártyák példányait tartalmazza.
        gombok: A kártyákhoz tartozó Tkinter gombok listája.
        elso_valasztas: Az elsőként kiválasztott kártya indexe a kártyalistában.
        lepesek_szama: Az eddigi lépések számlálója.

## Metódusok:

        __init__():
Inicializálja a Tkinter ablakot és a játék elemeit.
Létrehozza a kártyákat véletlenszerű sorrendben a random.shuffle segítségével.
Meghívja a felulet_letrehozasa() metódust a gombok elrendezésére.

        felulet_letrehozasa():
Rácsszerű elrendezésben elhelyezi a kártyákhoz tartozó gombokat a GUI-ban.
            A gombok mindegyikéhez egyedi eseménykezelőt (kartya_kattintas) rendel.

        kartya_kattintas(index):
Az adott indexű kártyához tartozó gomb megnyomásakor fut.
            Ha a kártya nincs felfordítva:
                Felfedi a kártya tartalmát.
                Ha ez az első választás, elmenti az indexet.
                Ha ez a második választás, egy másodpercre letiltja az összes gombot, majd ellenőrzi a párokat az ellenorzes metódussal.

ellenorzes(masodik_index):
            Összehasonlítja az elsőként és a másodikként kiválasztott kártyákat:
                Ha a kártyák megegyeznek, letiltja a gombokat.
                Ha nem egyeznek, visszaállítja a kártyák szövegét kérdőjellé, és felfordítva állapotukat False-ra.
            Ellenőrzi, hogy minden kártyát felfordítottak-e. Ha igen, győzelmi üzenetet jelenít meg.
            Visszaállítja a gombok állapotát a következő lépésekhez.

    run():
Elindítja a Tkinter fő eseménykezelő ciklusát.

## A program működése lépésről lépésre

Ablak létrehozása:
        A SzSzAMemoriaJatek osztály inicializálásakor a Tkinter ablak megnyílik, és a játékhoz szükséges elemek betöltődnek.

Kártyák inicializálása:
        Az emoji kártyák véletlenszerű sorrendben kerülnek egy listába (kartyak_lista).
        A lista elemeiből létrejön a kártyaobjektumokat tartalmazó kartyak lista.

Felület létrehozása:
        A gombok rácsban helyezkednek el a GUI-ban, mindegyik kártyához tartozik egy.

Játék indítása:
        A játékos rákattint egy gombra, amely felfedi a kártya tartalmát.
Ha két kártyát választ ki, az ellenorzes ellenőrzi, hogy egyeznek-e:
            Ha egyeznek, a kártyák aktív állapota megszűnik.
            Ha nem egyeznek, a kártyák visszafordulnak.

Győzelem ellenőrzése:
        Ha minden kártyát felfordítottak, egy győzelmi üzenet jelenik meg, és az alkalmazás bezárul.
