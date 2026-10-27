# Egyszerű Fájlkezeléses Python Projekt

## Hallgató
* **Név:** Vörös Richárd János
* **Neptun-kód:** G7KJNF

## Feladat leírása
A projekt egy grafikus felülettel rendelkező, egyszerű jegyzetkezelő és fájlkezelő alkalmazás Python nyelven. A program teljesíti az alábbi elvárásokat:
* Tartalmaz legalább egy tanult/bemutatandó modult (`os`), egy grafikus modult (`tkinter`) és egy saját készítésű modult (`sajat.py`)
* A bemutatásra szánt modul (`os`) legalább 3 különböző függvényét felhasználja és bemutatja
* Tartalmaz saját függvényeket, saját osztályokat, valamint grafikus eseménykezelést

## Modulok és a modulokban használt függvények
* **`os` modul (Beépített / bemutatandó modul):**
  * `os.path.exists()` – Ellenőrzi, hogy a megadott fájl létezik-e már a lemezen
  * `os.path.getsize()` – Lekérdezi a fájl méretét bájtokban
  * `os.getcwd()` – Visszaadja az aktuális munkamappa elérési útját

* **`tkinter` modul (Grafikus modul):**
  * `tk.Tk()`, `tk.Label`, `tk.Button`, `scrolledtext.ScrolledText`, `messagebox` – A felhasználói felület elemeinek és az ablakoknak a felépítésére szolgáló elemek

* **`sajat.py` (Saját modul):**
  * `VRJ_formatum(szoveg)` – Ellenőrzi, hogy a beírt szöveg nem üres-e
  * `VRJ_szoveg_forma(szoveg)` – Eltávolítja a felesleges szóközöket és üres karaktereket a szövegből

* **`foprogram.py` (Fő program modul):**
  * `mentes_kattintas()` – Eseménykezelő függvény a mentés gombhoz
  * `betoltes_kattintas()` – Eseménykezelő függvény a betöltés gombhoz
  * `os_funkciok_bemutatasa()` – Eseménykezelő függvény, amely megjeleníti az OS modul statisztikáit egy felugró ablakban
## Osztály(ok)
* **`JegyzetKezelo` osztály:** 
  A fizikai fájlkezelésért (szövegfájlba írás és abból olvasás) felelős osztály. Főbb metódusai: `mentes()` és `olvasas()`
* **`Alkalmazas` osztály:** 
  A grafikus felhasználói felület (GUI) felépítéséért, a widgetek elhelyezéséért és a gombok eseménykezelésének összekötéséért felelős fő osztály
