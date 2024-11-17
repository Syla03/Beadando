import tkinter as tk
from tkinter import messagebox
import random

class SzSzAKartya:

    def __init__(self, szoveg):
        self.szoveg = szoveg
        self.felforditva = False

class SzSzAMemoriaJatek:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SzSzA Memóriajáték")
        self.root.geometry("600x600")
        self.kartyak = []
        self.gombok = []
        self.elso_valasztas = None
        self.lepesek_szama = 0

        # Kártyák inicializálása
        self.kartyak_lista = list("🐻🐻🐔🐔🐉🐉🦏🦏🦍🦍🐎🐎🐅🐅🐢🐢")
        random.shuffle(self.kartyak_lista)
        self.kartyak = [SzSzAKartya(szoveg) for szoveg in self.kartyak_lista]
        self.felulet_letrehozasa()

    def felulet_letrehozasa(self):

        for index, kartya in enumerate(self.kartyak):
            gomb = tk.Button(
                self.root, text="?", width=8, height=4,
                font=("Arial", 16),
                command=lambda idx=index: self.kartya_kattintas(idx)
            )
            gomb.grid(row=index // 4, column=index % 4, padx=5, pady=5)
            self.gombok.append(gomb)

    def kartya_kattintas(self, index):

        kartya = self.kartyak[index]
        gomb = self.gombok[index]

        if not kartya.felforditva:
            gomb.config(text=kartya.szoveg)
            kartya.felforditva = True

            if self.elso_valasztas is None:
                self.elso_valasztas = index
            else:

                for btn in self.gombok:
                    btn.config(state="disabled")
                self.root.after(1000, self.ellenorzes, index)

    def ellenorzes(self, masodik_index):

        elso_index = self.elso_valasztas

        if elso_index is None:
            return

        kartya1 = self.kartyak[elso_index]
        kartya2 = self.kartyak[masodik_index]

        if kartya1.szoveg == kartya2.szoveg:
            self.gombok[elso_index].config(state="disabled")
            self.gombok[masodik_index].config(state="disabled")
        else:

            self.gombok[elso_index].config(text="?")
            self.gombok[masodik_index].config(text="?")
            kartya1.felforditva = False
            kartya2.felforditva = False

        self.elso_valasztas = None
        self.lepesek_szama += 1

        for btn, kartya in zip(self.gombok, self.kartyak):
            if not kartya.felforditva:
                btn.config(state="normal")


        if all(kartya.felforditva for kartya in self.kartyak):
            messagebox.showinfo("Győzelem", f"Gratulálok! Nyertél {self.lepesek_szama} lépésből!")
            self.root.destroy()
    def run(self):
        self.root.mainloop()
