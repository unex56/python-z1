vid = input("Вид питомца:")
age = int(input("Возраст(в годах):"))
klich = input("Кличка:")
if age % 10 == 1 and age % 100 != 11:
    year_word = "год"
elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
    year_word = "года"
else:
    year_word = "лет"
print(f'Это {vid} по кличке "{klich}". Возраст: {age} {year_word}')
