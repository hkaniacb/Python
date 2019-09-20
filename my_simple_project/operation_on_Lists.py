# Dwie metody sortowanaia jedna przy użycia lambda, druga przy użyciu fukncji zwracającej odpowiednią wartość

    data = [
        ["Fruit", "Quantity"],
        ["Kiwi", 3],
        ["Grape", 15],
        ["Apple", 5],

    ]
    print("Przed sortowaniem: ")
    print(data)
    data.sort(key=lambda x: x[0]) # lambda prawdopodobie mapuję wewnetrzna listę
    print("Po sortowaniu: ")
    print(data)

    ls2=[[0,1,'f'],[4,5,'t'],[9,4,'afsd']]
    def thirdItem(ls): # funkcja zwaracajaca zagnieżdzony element  listy o podanym idenksie
        return ls[2]
    print("Przed sortowaniem: ")
    print(ls2)
    ls2.sort(key=thirdItem)
    print("Po sortowaniu: ")
    print(ls2)
