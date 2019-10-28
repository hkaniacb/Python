def czwarta(f):
    def wewn(liczba):
        print("Jestem funkcja wewnetrza")
        wynik = f(liczba)
        return wynik**2
    return wewn

@czwarta # dekorator zwraca funkcje pierwsza(n) jako parametr f  # Ponizsza funkcja jest zwracana do powyżej
def pierwsza(n):
    return n*2

print(pierwsza(5))
