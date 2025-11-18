from random import Random, choice
import passstrassen

def anzahlPassstrassen() -> int:
    return len(passstrassen.SchweizerPassstrasse)

def passAnfangEnde(von, nach):
    for passname, passdaten in enumerate(passstrassen.SchweizerPassstrasse.items()):
        if (passdaten['von'] == von and passdaten['nach'] == nach):
            return passname
        else:
            None
        
def passVonNach(von, nach) -> str:
    return next(
        (passname for passname, passdaten in passstrassen.SchweizerPassstrasse.items()
         if passdaten['von'] == von and passdaten['nach'] == nach),
        None
    )

def main():
    
    print(f"Grösse der DB: {anzahlPassstrassen()} Pässe sind eingetragen")
    print(passVonNach('Andermatt', 'Disentis'))

    data = passstrassen.SchweizerPassstrasse
    data.keys()

    aPick = choice(list(data.keys()))
   
    print(f"Zufälliger Passname: {aPick}")
    # DEBUG: print(data.get(aPick))
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


  # print(passstrassen.SchweizerPassstrasse.items())

if __name__ == '__main__':
    main()

