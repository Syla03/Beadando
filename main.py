from szsza_memoria import SzSzAMemoriaJatek  # Importáljuk a memóriajáték osztályt a szsza_memoria modulból

def main():
    """Főfüggvény a játék indításához"""
    print("Memóriajáték indítása...")  # Konzolra kiír egy üzenetet, hogy a játék indul
    app = SzSzAMemoriaJatek()  # Létrehozza a memóriajáték alkalmazás példányát
    app.run()  # Elindítja a játékot (Tkinter fő eseményciklusát)


if __name__ == "__main__":
    main()  # Ellenőrzi, hogy a script közvetlenül fut-e, és ha igen, meghívja a main függvényt
