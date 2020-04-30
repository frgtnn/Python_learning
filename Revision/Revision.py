#Zrob wymyslona liste, wypisz mi pierwszy elementy, ostatni, od trzeciego do szóstego
#Wyświetl mi długość listy pomnozona przez 5
lista_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(lista_1[0])
print(lista_1[-1])
print(lista_1[2:5])
print(len(lista_1*5))
#Wyświetl kwadraty liczb od 0 do 11
for i in range(0, 11):
    print(i**2)
#Wyswietl kazdy element powiekszony o swoj pierwiastek (oczywiscie potrzebujesz import math) 2) Wyswietl pierwsze 4 elementy pomniejszone o sinus(3.14)
numbers = [12.3 ,1 , -23, 23.1, -5, -6, 4, 67, 8, 10, -45]
import math
for num in numbers:
    if num > 0:
        print(num+(math.sqrt(num)))
#Wyswietl pierwsze 4 elementy pomniejszone o sinus(3.14)
for num in range(0, 4):
    print(numbers[num]-(math.sin(3.14)))
