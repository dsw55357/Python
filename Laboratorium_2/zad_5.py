# 5. Napisz program „symulator badania alkomatem”, który po podaniu odpowiednich wartości
# w wydychanym powietrzu(zgodnie z przepisami prawa) wskaże stan nietrzeźwości
# i stan po użyciu alkoholu zgodnie z przepisami prawa.

def main():
    
    # Pobranie wartości w mg
    poziom = float(input("Podaj wartość pomiaru [mg/l]: "))

    if poziom < 0.1:
        print("Stan: zdrowy")
    elif poziom >= 0.1 and poziom <= 0.25:
        print("Stan: po spożyciu alkoholu!")
    elif poziom > 0.25:
        print("Stan: nietrzeźwości!!")

if __name__ == "__main__":
    
    main()
