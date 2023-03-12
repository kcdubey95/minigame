# guss the number
from random import randint


def guess_number():
    randam_number = randint(0, 9)
    input_number = -1
    print(randam_number)
    while input_number != randam_number:
        if input_number != -1:
            print("Wrong Number")
        input_number = int(input("Guess Number"))
        if input_number == randam_number:
            print("You guess Right N5umber")


# guess_number()

def quiz_do():
    questions = ["Who got the first Oscar award in India?",
                 "Who is known as the Father of Indian cinema?",
                 "Who is known as the Father of Indian cinema?"]
    ans = [
        "bhanu athaiya",
        "dhundiraj govind",
        "dangal"]
    score = 0
    for i in range(0, len(questions)):
        print(questions[i])
        user_ans = input("Write Your ans")
        print(user_ans.lower())
        if user_ans.lower() == ans[i]:
            print("Correct ANS")
            score = score + 1
        else:
            print("Wrong ans")

    print(f"score {score}")


#guess a word
def guess_word():
    word = "india"
    word_collection = []
    max_attemp = 0

    while True:
        your_letter = input("try your word").lower()

        if your_letter in word:
            word_collection.append(your_letter)
            max_attemp = max_attemp + 1
            if max_attemp == 5:
                data=listTostring(word_collection)

                if data=='india':
                    print("You won")
                    break
                else:
                    break

        else:
            max_attemp = max_attemp + 1
            if max_attemp >= 5:
                break


def listTostring(list):
    str = ""
    for i in list:
        str += i
    return str

guess_word()