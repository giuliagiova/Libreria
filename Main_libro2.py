from Libro2 import AggiuntaLibro, PrestitoLibro, RiportaLibro, DisponibilitàLibro, LibriDisponibili, LibriInPrestito

libri = []

libriprestito = []

while True: 
    print("Libreria")
    print("1) Aggiunta libro")
    print("2) Prestito libro")
    print("3) Riporta libro")
    print("4) Disponibilità libro")
    print("5) Libri disponibili nella libreria")
    print("6) Libri dati in prestito")
    print("7) Uscita")

    scelta = int(input("Digita un numero tra 1 e 7: "))

    if scelta == 1: 
        AggiuntaLibro(libri)
    elif scelta == 2: 
        PrestitoLibro(libri, libriprestito)
    elif scelta == 3:
        RiportaLibro(libri, libriprestito)
    elif scelta == 4:
        DisponibilitàLibro(libri)
    elif scelta == 5:
        LibriDisponibili(libri)
    elif scelta == 6:
        LibriInPrestito(libriprestito)
    elif scelta == 7:
        print("Programma terminato")
        break
    else: 
        print("Inserisci un numero tra 1 e 7")
