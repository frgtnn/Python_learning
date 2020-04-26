# print(len(courses)) - liczba kursow
# print(courses[3]) - program pokazuje konkretna wartosc po kolei #liczone sa od zera
# print(courses[-1]) - wymienia konkretna wartosc od konca
# print(courses[0:2])/print(courses[:2]) <- is the same #wymienia wartosci od 0 do 2, ale nie zawiera ostatniej wartosci
# print(courses[2:]) od dwojki az do konca
# courses.append('Art') - dodawanie wartosci do liczby kursow
# courses.insert(0, 'Art') #wstawianie kursu #Art na sam poczatek wartosci 'Courses'
#courses_2 = ['Art', 'Education'] # courses.insert(0, courses_2) wstawienie nowej listy do naszej starej listy przy uzyciu komendy 'insert'
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']
# courses.extend(courses_2) wykonujac to i dodajac na koniec print(courses) dostajemy wynik w postaci naszej listy nr 1
#dodawana jest automatycznie dzieki komendzie 'extend' kolejna lista
#courses.remove('value') #usuwanie konkretnej wartosci z naszego kodu
# courses.pop() #ostatnia wartosc jest wyrzucana z listy
#popped = courses.pop()
#print(popped)
#print(courses) #komenda ta pozwala nam na zauwazenie jaka linijka programu zostala wyrzucona z naszej listy
#courses.reverse() #lista pokazuje sie od konca do poczatku
#courses.sort() #lista jest sortowana wg alfabetu
# courses.sort() dodajac komende(reverse=True) pozwala to na sortowanie liczb czy list od tylu
# nums.sort() dodajac komende(reverse=True) pozwala to na sortowanie liczb czy list od tylu
# print(courses)
# print(nums) # ta linijka pozwala nam na grupowanie liczb oraz listy alfabetycznie
#sorted_courses = sorted(courses)
# print(sorted_courses) pozwala nam na sortowanie listy bez ingerencji w nia
#print(sum/min/max(nums)) #suma/minimalna/maksymalna
#print(courses.index('CompSci')) #dostajemy informacje zwrotna na ktorej pozycji znajduje sie dana wartosc,
#jak czegos nie bedzie na liscie, wywali error
#print('Art' in courses) #sprawdzanie czy cos jest na liscie True/False
#for item in courses: #jezeli uzyjemy 'for courses in courses: #print(courses) dostaniemy taki sam wynik
    #print(item) #pokazuje nam w jednej linii wszystkie wartosci ktore znajduja sie w 'courses'
# for index, course in enumerate(courses, start=liczba #daje nam od jakiej wartosci sa liczone wartosci w liscie):
#     print(index, course)  #przedstawia nam w jakiej kolejnosci sa wartosci zawarte w naszej liscie
# course_str = ' - '.join(courses)
# print(course_str) #mowi programowi w jaki sposob maja byc od siebie oddzielone wartosci

# course_str = ' - '.join(courses)
# new_list = course_str.split(' - ')
# print(course_str)
# print(new_list) #pozwala na powrot z rozdzielonego stringa#ciagu znakow mylsnikami, do listy []

#Zmienne (Mutable)
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2) po prostu lista 1 rowna sie liscie 2 #list_1[0] = 'Art' - dodajemy do obu list nowa zmienna 'Art' na sam poczatek list
#cause they are mutable objects

#Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

#Sets - lista wyswietla sie randomowo - jezeli cos sie powtarza, bedzie i tak wyswietlane pojedynczo
# print('Math' in cs_courses) #sety sa zoptyamlizowane z komenda in courses T/F
# print(cs_courses.intersection(art_courses)) #sprawdzanie jakie wartosci znajduja sie w obu listach
# print(cs_courses.difference(art_courses)) #sprawdzenie jakie sa roznice
# print(cs_courses.union(art_courses)) #wszystkie wartosci z dwoch list w jednej liscie
# cs_courses = {'History', 'Math', 'Physics', 'CompSci',}
# art_courses = {'History', 'Math', 'Art', 'Design',}
# print(cs_courses.intersection(art_courses))

#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} #This isnt right. Its a dict
empty_set = set()






