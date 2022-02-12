import random
import string

n_znakow = int(input("podaj dlugosc hasla: "))
n_znakow_typu = 2 #iloć znakow z kazdego dostepnego rodzaju
roznica_znakow = int(n_znakow) - int(n_znakow_typu * 4)

lower_case= string.ascii_lowercase  #od a do z male litery
upper_case= string.ascii_uppercase #od a do z duzej litery
punctuation= string.punctuation # znaki specjalne
digits = string.digits # cyfry
wszystkie_znaki = lower_case + upper_case + punctuation + digits

wymagane_znaki = random.choices(lower_case,k=n_znakow_typu) + random.choices(upper_case,k=n_znakow_typu) + random.choices(punctuation,k=n_znakow_typu) + random.choices(digits,k=n_znakow_typu)
wymagane_uzupelniajace_znaki = random.choices(wszystkie_znaki,k = roznica_znakow)
haslo = wymagane_znaki + wymagane_uzupelniajace_znaki
random.shuffle(haslo)
haslo = ''.join(haslo)

print()
print(haslo)

