#!/usr/bin/env python3
import random
import prompt


def main():
    pass


order_list = 0
flag = True
rand_list = list(zip(
    [random.randrange(1, 20, 1) for i in range(3)],
    [random.randrange(1, 20, 1) for i in range(3)]
))


name = prompt.string('''Welcome to the Brain Games!
May I have your name?   ''')    # Приглашение к вводу имени
print('What is the result of the expression?')


def gcd(first_number, second_number):
    if first_number == 0 or second_number == 0:
        return first_number + second_number
    elif first_number > second_number:
        return gcd(first_number - second_number, second_number)
    else:
        return gcd(first_number, second_number - first_number)


def question(first_number, second_number):
    global flag
    print('Question:  ' + str(first_number) + ' ' + str(second_number))
    answer = input('Your answer: ')
    if answer == str(gcd(first_number, second_number)):
        print('Correct!')
        flag = True
        return flag
    elif answer != str(gcd(first_number, second_number)):
        print(f'{answer} is wrong answer ;(. Correct answer was {gcd(first_number, second_number)}.')
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
