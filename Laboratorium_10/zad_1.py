"""

tekst = f"Na podstawie poniższego cytatu z „Wiedźmina”
„Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć
zakazane drzwi. Drzwi, za którymi czai się koszmar, zgroza i niewyobrażalna okropność,
za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nie
tylko tego, kto drzwi te uchyli, ale i cały świat. A ponieważ nie brakuje takich, którzy przy
owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada świata będzie
przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po
Koniunkcji Sfer ludzie nauczyli posługiwać się magią, jest przekleństwem i zgubą świata.
Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się.”Przetestuj metody : lower() , swapcase(), capitalize() , replace(), lstrip(), rstrip(),
reversed(),count(),find(), isalnum(), starswith(),endswith(). Zastosuj odpowiednie
formatowanie przy użyciu f-stringów."

"""

tekst = f"Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć\
        zakazane drzwi. Drzwi, za którymi czai się koszmar, zgroza i niewyobrażalna okropność,\
        za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nie\
        tylko tego, kto drzwi te uchyli, ale i cały świat. A ponieważ nie brakuje takich, którzy przy\
        owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada świata będzie\
        przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po\
        Koniunkcji Sfer ludzie nauczyli posługiwać się magią, jest przekleństwem i zgubą świata.\
        Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się.”Przetestuj metody : lower() , swapcase(), capitalize() , replace(), lstrip(), rstrip(),\
        reversed(),count(),find(), isalnum(), starswith(),endswith(). Zastosuj odpowiednie\
        formatowanie przy użyciu f-stringów."

def main():

    lower = tekst.lower()
    print(f"Lower:\n {lower}")

    swap = tekst.swapcase()
    print(f"Swap:\n {swap}")

    cap = tekst.capitalize()
    print(f"Cap:\n {cap}")

    replace = tekst.replace('k', 'a')
    print(f"Replace:\n {replace}")

    lstrip = tekst.lstrip()
    print(f"Lstrip:\n {lstrip}")

    rstrip = tekst.rstrip()
    print(f"Rstrip:\n {rstrip}")

    count = tekst.count(' ')
    print(f"Count:\n {count}")

    find = tekst.find('a')
    print(f"Find:\n {find}")

    isa = tekst.isalnum()
    print(f"Isa:\n {isa}")

    start = tekst.startswith("M")
    print(f"Start:\n {start}")

    end = tekst.endswith("a")
    print(f"End:\n {end}")
    
if __name__ == "__main__":
    
    main()