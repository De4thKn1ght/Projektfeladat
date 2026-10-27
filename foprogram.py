
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
import sajat

class JegyzetKezeloVRJ:

  def __init__(self, fajlnev="jegyzet.txt"):
    self.fajlnev = fajlnev

  def mentes(self, szoveg):
    with open(self.fajlnev, "w", encoding="utf-8") as f:
      f.write(szoveg)

  def olvasas(self):
    if os.path.exists(self.fajlnev):
      with open(self.fajlnev, "r", encoding="utf-8") as f:
        return f.read()
    return ""

class Alkalmazas:

  def __init__(self, root):
    self.root = root
    self.root.title("Egyszerű Fájlkezelő Program")
    self.root.geometry("450x400")

    self.kezelo_VRJ = JegyzetKezelo()

    self.cimke = tk.Label(
        root, text="Írd be a jegyzetedet alább:", font=("Arial", 11)
    )
    self.cimke.pack(pady=5)

    self.szoveg_doboz = scrolledtext.ScrolledText(
        root, width=50, height=12, font=("Arial", 10)
    )
    self.szoveg_doboz.pack(pady=5)

    self.mentes_gomb = tk.Button(
        root,
        text="Mentés Fájlba",
        command=self.mentes_kattintas,
        bg="lightgreen",
        width=30,
    )
    self.mentes_gomb.pack(pady=3)

    self.betoltes_gomb = tk.Button(
        root,
        text="Fájl Betöltése",
        command=self.betoltes_kattintas,
        bg="lightblue",
        width=30,
    )
    self.betoltes_gomb.pack(pady=3)

    self.statisztika_gomb = tk.Button(
        root,
        text="Fájl Infó (OS modul)",
        command=self.os_funkciok_bemutatasa,
        bg="lightyellow",
        width=30,
    )
    self.statisztika_gomb.pack(pady=3)

    meglevo_szoveg = self.kezelo.olvasas()
    if meglevo_szoveg:
      self.szoveg_doboz.insert(tk.END, meglevo_szoveg)

  def mentes_kattintas(self):
    szoveg = self.szoveg_doboz.get("1.0", tk.END)

    if sajat.formatum_ellenorzo(szoveg):
      tiszta_szoveg = sajat.szoveg_formazasa(szoveg)
      self.kezelo.mentes(tiszta_szoveg)
      messagebox.showinfo("Siker", "A jegyzet sikeresen mentve a fájlba!")
    else:
      messagebox.showwarning("Figyelmeztetés", "Nem menthetsz üres mezőt!")

  def betoltes_kattintas(self):
    szoveg = self.kezelo.olvasas()
    self.szoveg_doboz.delete("1.0", tk.END)
    self.szoveg_doboz.insert(tk.END, szoveg)
    messagebox.showinfo("Siker", "Jegyzet betöltve a fájlból!")

  def os_funkciok_bemutatasa(self):
    """Bemutatásra szánt modul (os) legalább 3 függvénye:

    1. os.path.exists()
    2. os.path.getsize()
    3. os.getcwd()
    """
    fajl = self.kezelo.fajlnev

    letezik = os.path.exists(fajl)

    meret = os.path.getsize(fajl) if letezik else 0

    aktualis_mappa = os.getcwd()

    uzenet = (
        f"Fájl neve: {fajl}\n"
        f"Létezik a fájl?: {letezik}\n"
        f"Fájl mérete: {meret} bájt\n"
        f"Aktuális mappa: {aktualis_mappa}"
    )
    messagebox.showinfo("OS Modul Statisztika", uzenet)


if __name__ == "__main__":
  root = tk.Tk()
  app = Alkalmazas(root)
  root.mainloop()