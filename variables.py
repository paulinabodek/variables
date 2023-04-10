# wallet = 41

# print(wallet)

# wallet = 32

# print(wallet)

# day = 21

# temp = -15

# weight = 169.4

# print(3 + 6)

# print(day+3)

# print(weight *2)

# print(weight/2)

# age = 37

# euro = 4.67

# shirt = "green"

# print(shirt)

# store = 'James\'s Pizza Shop, the "best" there is'

# print(store)

# movie = 'Independence day, the "best" movie is'

# print(movie)

# day = 21
# month = "october"
# temp = 65

# print(f"Today is {month} {day} and it's {temp} degrees outside")

# day = 3
# name_day = "tuesday"
# year = 2022

# print(f"Today is {day} {name_day} {year}")

# light_is_on = True

# if light_is_on:
#     print("The light is on!")

# wardrobe_is_on = False

# if wardrobe_is_on:
#     print("wardrobe is on!")
# else:
#     print("We're in the dark")

# weight = 165.4

# if weight < 170:
#     print("You're under weight :)")

# age = 19

# if age >= 18:
#     print("You are an adult")
# if age <18:
#     print("You are a child")

# import random

# print(random.randint(1,10))

# print(random.random())

# answer = random.randint(1,3)

# if answer == 1:
#     print("yes")
# if answer == 2:
#     print("no")
# if answer == 3:
#     print("maybe")

# import random

# lucky_number = random.randint(1,100)

# fortune_number = random.randint(1,3)

# fortune_text = ''

# if fortune_number == 1:
#     fortune_text = 'You will have a great day!'
# if fortune_number == 2:
#     fortune_text = 'Today will be tough...but worth it.!'
# if fortune_number == 3:
#     fortune_text = 'You will get married this year!'

# print(f'{fortune_text} Your lucky numer is: {lucky_number}')

# fav_movies = ["Sandlot", "Dune"]

# print(fav_movies[0])

# fav_numbers = ["7", "8"]

# print(fav_numbers[0])

# print(len(fav_movies))

# fav_movies.append("Iron Man")

# print(len(fav_movies))

# print(fav_movies)

# fav_movies.insert(1,"Batman")

# print(fav_movies)

# del(fav_movies[2])

# print(fav_movies)

# del(fav_movies[0])
# del(fav_movies[0])

# print(fav_movies)

# number_one = 2

# number_two = 3

# print(number_one + number_two)

# for number in range(10):
#     print("Hello")
#     print(number)

# fav_movies = ["Sandlot", "Dune"]

# for movie in fav_movies:
#     print(movie)

# for number in range(40):
#     print(number  * 2)

# cats = {"Jane":6, "Tom":14, "Sara":8}

# cats["Wilson"] = 1

# del(cats["Tom"])

# print(cats)

# ints_and_bools = {1:True, 0:False}

# text = """Drzewko bonsai to inaczej karłowate drzewo w naczyniu, otrzymywane metodą miniaturyzowania roślin. Proces ten wiąże się z wieloletnią pracą polegającą na regularnym przycinaniu pędu drzewka i jego pielęgnacji. Najbardziej cenionymi drzewkami bonsai są te stworzone z długowiecznych dębów, cisów, sosen czy jałowców. Ich cechą rozpoznawczą jest charakterystyczne pochylenie pnia drzewka ku doniczce."""
# print(len(text))
# print(text.split())
# print(len(text.split()))

# text = """
# a b c a a b
# """

# print(text.split())

# word_count = {}

# for word in text.split():
#     print(word)



text = """
Doświadczeni hodowcy bonsai radzą spryskiwanie całego drzewka wodą, a nie bezpośrednie podlewanie ziemi w doniczce. Zbyt duża ilość wody może doprowadzić do gnicia korzeni. Ziemia, w której rośnie bonsai, powinna być stale lekko wilgotna. Drzewku bonsai nie służy zarówno przelanie jak i przesuszenie
"""

print(text.split())

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(word_count)
