import random
import string
from unicodedata import digit

n_znakow = int(input("podaj dlugosc hasla: "))
n_znakow_typu = 2
roznica_znakow = int(n_znakow) - int(n_znakow_typu * 4)

lower_case= string.ascii_lowercase  #od a do z male litery
upper_case= string.ascii_uppercase #od a do z duzej litery
punctuation= string.punctuation # znaki specjalne
digits = string.digits
wszystkie_znaki = lower_case + upper_case + punctuation + digits

wymagane_znaki = random.choices(lower_case,k=n_znakow_typu) + random.choices(upper_case,k=n_znakow_typu) + random.choices(punctuation,k=n_znakow_typu) + random.choices(digits,k=n_znakow_typu)
wymagane_uzupelniajace_znaki = random.choices(lower_case,k = roznica_znakow)
haslo = wymagane_znaki + wymagane_uzupelniajace_znaki
random.shuffle(haslo)
haslo = ''.join(haslo)

print()
print(haslo)




#TODO: 
# progaram ma sprawic ze wygeneruje nam hasło
# Założenia : string -ciag znakow
# - Hasło ma być losowe
# - Wytyczne co ma byc w hasle:
# - min 8 znaków , duże litery - 2, małe litery -2 , znaki specjalne -2, cyfry -2
#zadanie domowe 1 udoskonal generator haseł tak aby 
###- 1 brał po 2 losowe cyfry/znaki/małe i duże litery
# 2 zeby była losowa kolejność tych wszystkich typów danych cyfry/znaki/małe i duże litery
# 3 co robić aby to działało dobrze dla zadanej liczby znaów od 8 - 20 czyli podajemy 8 lub 20 znkow i działa za każdym razem dobrze na 8 i pomiedzy 20
#FIXME:
#
# zadanie domowe spraw aby ten generatoł haseł wystapił na naszej stronie internetowej pod adressem /generator_hasel
# zrób u siebie na serwerze, poczytaj jak z vs wrzucic na gita  
#



#print(wymagane_uzupelniajace_znaki)

#print(haslo[0], type(haslo[0]))

#cos nie dzialalo bo do konca nie przeczytalem
# haslo = ''
# for i in range[10]:
#         haslo +=random.sample(lower_case, 1[0])
# print(haslo)

# wersja z forem
# for c in ciag:
#     c+= 'xyz'
#     x = len(c)
#     print(c,x)

# if 'a' in ciag:
#     print("OK")
# elif'abc' in ciag:
#     print('2 ok')

# upper_case = string.ascii_uppercase 
# digits = string.digits