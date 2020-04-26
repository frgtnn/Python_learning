#print(student['name']) #pokazuje konkretne wartosci z listy "student" #namestr, #ageint, #courseslist
#print(student.get('phone')) #jezeli lista nie posiada 'phone' dostaniemy odp. 'none' zamiast erroru
#after 'phone', 'Not Found' w tym momencie program odpowie nam tak jak chcemy tj. mozemy stworzyc konkretna odp.
# student['name'] = 'Jane' - mozemy dzieki temu zmienic wartosc w poprzedniej komendzie John zmienia sie na Jane
#student.update - jedna komenda mozemy zmienic wartosci z komendy "student"
# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
#del student['value'] usuwanie konkretnej wartosci z listy
#student.pop('value') - wyrzucenie konkretnej wartosci do nastepnej linjki tekstu z listy
#print(student.keys()) zwraca legende, returns keys
# print(student.values()) #daje wartosci tj. imie, wiek, kursy
#print(student.items()) #returns all of the values
# for key in student:
#     print(key) returns
# for key, value in student.items():
#     print(key, value) # key returns names etc., value gives answer John, 25, etc.
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)