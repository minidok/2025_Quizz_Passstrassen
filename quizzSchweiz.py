from random import Random, choice
from passstrassen import SchweizerPassstrasse

def anzahlPassstrassen() -> int:
    return len(SchweizerPassstrasse)

def passAnfangEnde(von, nach):
    for passname, passdaten in SchweizerPassstrasse.items():
        if passdaten['von'] == von and passdaten['nach'] == nach:
            return passname
    return None
        
def passVonNach(von, nach) -> str:
    return next(
        (passname for passname, passdaten in SchweizerPassstrasse.items()
         if passdaten['von'] == von and passdaten['nach'] == nach),
        None
    )

def main():
    
    print(f"Grösse der DB: {anzahlPassstrassen()} Pässe sind eingetragen")
    # DEBUG: Ausgabe Oberalppass
    #print(passVonNach('Andermatt', 'Disentis'))

    data = SchweizerPassstrasse
    data.keys()

    aPick = choice(list(data.keys()))
   
    print(f"Zufälliger Passname: {aPick}")
    # DEBUG: print(data.get(aPick)) gibt einen ganzen Datensatz aus.
    print(data.get(aPick))

    print(f"In welchem Kanton, ist der Pass: {aPick} ?")
    AntwortBenutzer = input("Ihre Antwort: ")
    AntwortBenutzer = AntwortBenutzer.lower()
    richtigeAntwort = data.get(aPick)['Kanton'].lower()

    if AntwortBenutzer == richtigeAntwort:
        print("Richtig")   
    else:  
        print("Falsch")
        print(f"Die richtige Antwort ist: {richtigeAntwort}")

if __name__ == '__main__':
    main()

