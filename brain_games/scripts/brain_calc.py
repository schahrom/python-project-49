#!/usr/bin/env python3
import random
import prompt


def main():
    pass


order_list = 0
flag = True
letters_container = '-+*'
rand_list = list(zip(
    [random.randrange(1, 50, 1) for i in range(3)],
    [random.randrange(1, 50, 1) for i in range(3)]
))


name = prompt.string('''Welcome to the Brain Games!
May I have your name?   ''')    # Приглашение к вводу имени
print('What is the result of the expression?')


def question(first_number, second_number):
    global flag
    question_template = str(first_number) + ' ' + random.choice(letters_container) + ' ' + str(second_number)
    answer = '' + question_template
    print('Question:  ' + question_template)
    answer = input('Your answer: ')
    if answer == str(eval(question_template)):
        print('Correct!')
        flag = True
        return flag
    elif answer != str(eval(question_template)):
        print(f'{answer} is wrong answer ;(. Correct answer was {eval(question_template)}.')
        flag = False
        return flag
    else:
        print('Wrong answer.')
        flag = False
        return flag


while flag is True:
    if order_list <= 2:
        question(rand_list[order_list][0], rand_list[order_list][1])
        order_list += 1
    elif order_list > 2:
        print(f'Congratulations, {name}!!!')
        break

if flag is False:
    print(f"Let's try again, {name}!")
