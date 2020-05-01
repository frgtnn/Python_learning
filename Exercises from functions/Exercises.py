a = 12
b = 3
def multiply(a,b):
    return a*b
wynik = multiply(a,b)
print(wynik)

tab = [1, 23, 53, 12, 24, 20, 4, 6, -23, 23, -4, 200]
# def wypisz_liczby(jakas_tablica):
#     for numer in jakas_tablica:
#         print(numer)
# wypisz_liczby(tab)

# def only_positive(array):
#     for num in array: deklaracja funckji (array) moze byc czymkolwiek

def only_positive(array):
    for num in array:
        if num < 0:
            print(num)

only_positive(tab)

def wypisz_3(array):
    print(array[:3])

wypisz_3(tab)

def wypisz_3_powiekszone(tab):
    for i in range(3):
        print(tab[i]+14)

wypisz_3_powiekszone(tab)

#dodawanie elemntow na koniec listy
# tab_2 = []
# tab_2.append(2)
# print(tab_2)
# tab_2.append(4)
# print(tab_2)

def only_plus_10(array):
    new_tab = []
    for element in array:
        if element < 10:
            new_tab.append(element)

    return new_tab

wynik = only_plus_10(tab)
print(wynik)

arr1 = [2, 4, 10]
arr2 = [4, 5, 60]

def array_plus_array(arr1, arr2):
    length = len(arr1)
    suma = 0
    for i in range(length):
        suma += arr1[i] + arr2[i]
    return suma
wynik = array_plus_array(arr1, arr2)
print(wynik)