import tkinter as tk  # Tkinter modul az ablak és GUI elemek kezeléséhez
from tkinter import messagebox  # Felugró ablakok kezelésére szolgál
import random  # Véletlenszerű elemek generálására, például a kártyák keverésére

class SzSzAKartya:
    """Kártya osztály"""
    def __init__(self, szoveg):
        self.szoveg = szoveg  # A kártya tartalma (például 🐻)
        self.felforditva = False  # Boolean: jelzi, hogy a kártya felfordított állapotban van-e

class SzSzAMemoriaJatek:
    """Memóriajáték osztály"""
    def __init__(self):
        self.root = tk.Tk()  # Fő Tkinter ablak inicializálása
        self.root.title("SzSzA Memóriajáték")  # Ablak címe
        self.root.geometry("600x600")  # Ablak mérete
        self.kartyak = []  # Lista a kártyaobjektumok tárolására
        self.gombok = []  # Lista a kártyákhoz tartozó gombok tárolására
        self.elso_valasztas = None  # Az elsőként választott kártya indexe
        self.lepesek_szama = 0  # Lépésszámláló

        # Kártyák inicializálása
        self.kartyak_lista = list("🐻🐻🐔🐔🐉🐉🦏🦏🦍🦍🐎🐎🐅🐅🐢🐢")  # Páros kártyák listája
        random.shuffle(self.kartyak_lista)  # Kártyák véletlenszerű sorrendbe rendezése
        self.kartyak = [SzSzAKartya(szoveg) for szoveg in self.kartyak_lista]  # Kártyaobjektumok létrehozása

        self.felulet_letrehozasa()  # A játékfelület létrehozása

    def felulet_letrehozasa(self):
        """A játék felületének létrehozása"""
        for index, kartya in enumerate(self.kartyak):  # Végigmegyünk a kártyákon
            gomb = tk.Button(
                self.root, text="?", width=8, height=4,  # Gomb mérete
                font=("Arial", 16),  # Gomb betűtípusa és mérete
                command=lambda idx=index: self.kartya_kattintas(idx)  # Minden gombhoz eseménykezelő
            )
            gomb.grid(row=index // 4, column=index % 4, padx=5, pady=5)  # Gombok rácsban elrendezve
            self.gombok.append(gomb)  # Gomb hozzáadása a gombok listájához

    def kartya_kattintas(self, index):
        """Kattintás esemény kezelése"""
        kartya = self.kartyak[index]  # A kattintott kártya
        gomb = self.gombok[index]  # A kattintott kártyához tartozó gomb

        if not kartya.felforditva:  # Ha a kártya nincs felfordítva
            gomb.config(text=kartya.szoveg)  # Felfedjük a kártya tartalmát
            kartya.felforditva = True  # Állapot: felfordítva

            if self.elso_valasztas is None:  # Ha ez az első választás
                self.elso_valasztas = index  # Elmentjük az indexet
            else:
                # Második kattintás - ideiglenesen letiltjuk a gombokat
                for btn in self.gombok:
                    btn.config(state="disabled")
                self.root.after(1000, self.ellenorzes, index)  # 1 másodperc múlva ellenőrzés

    def ellenorzes(self, masodik_index):
        """Kártyapárok ellenőrzése"""
        elso_index = self.elso_valasztas  # Az első kártya indexe

        if elso_index is None:  # Ha nincs első kártya, kilépünk
            return

        kartya1 = self.kartyak[elso_index]  # Első kártya
        kartya2 = self.kartyak[masodik_index]  # Második kártya

        if kartya1.szoveg == kartya2.szoveg:  # Ha a két kártya egyezik
            self.gombok[elso_index].config(state="disabled")  # Az első gombot letiltjuk
            self.gombok[masodik_index].config(state="disabled")  # A második gombot is letiltjuk
        else:
            # Ha nem egyeznek, visszaállítjuk a kártyákat
            self.gombok[elso_index].config(text="?")  # Első gomb szövegét visszaállítjuk
            self.gombok[masodik_index].config(text="?")  # Második gomb szövegét is
            kartya1.felforditva = False  # Első kártyát lefordítjuk
            kartya2.felforditva = False  # Második kártyát is lefordítjuk

        self.elso_valasztas = None  # Első választás törlése
        self.lepesek_szama += 1  # Lépésszámláló növelése

        # Visszaállítjuk az engedélyezést a még nem felfordított gombokra
        for btn, kartya in zip(self.gombok, self.kartyak):
            if not kartya.felforditva:
                btn.config(state="normal")

        # Ellenőrizzük, hogy minden kártya felfordult-e
        if all(kartya.felforditva for kartya in self.kartyak):  # Ha minden kártya felfordítva
            messagebox.showinfo("Győzelem", f"Gratulálok! Nyertél {self.lepesek_szama} lépésből!")  # Győzelmi üzenet
            self.root.destroy()  # Alkalmazás bezárása

    def run(self):
        """Az alkalmazás futtatása"""
        self.root.mainloop()  # Tkinter eseménykezelő ciklus indítása
