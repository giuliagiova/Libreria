def AggiuntaLibro(libri):
    libro = input("Inserisci il titolo del libro: ")
    libri.append(libro)
    print(f"Ha inserito il libro: {libro}")

def PrestitoLibro(libri, libriprestito):
    libro = input("Inserisci il titolo del libro che vuoi in prestito: ")
   
    if libro in libri: 
        libri.remove(libro)
        libriprestito.append(libro)
        print(f"Hai preso in prestito il libro: {libro}")
    else:
        print("Il libro non è disponile")

def RiportaLibro(libri, libriprestito):
    libro = input("Inserisci il titolo del libro che vuoi restituire: ")
    libri.append(libro)
    libriprestito.remove(libro)
    print(f"Hai restituito il libro: {libro}")

def DisponibilitàLibro(libri):
    libro = input("Di quale libro vuoi verificare la disponibilità? ")
    if libro in libri: 
        print("Il libro è dispobile")
    else:
        print("Il libro non è disponibile")
    
def LibriDisponibili(libri):
    for libro in libri:
        print(libro)

def LibriInPrestito(libriprestito):
    for libro in libriprestito:
        print(libro)
   
