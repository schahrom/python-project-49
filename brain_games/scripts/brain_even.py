#!/usr/bin/env python3
import random
import prompt


def main():
    pass


name = prompt.string('''Welcome to the Brain Games!
May I have your name?   ''')    # Приглашение к вводу имени


order_list = 0
flag = True
rand_list = [random.randrange(1, 50, 1) for i in range(3)]
print('Answer "yes" if the number is even, otherwise answer "no".')


def its_even(number):
    return True if rand_list[number] % 2 == 0 else False


def for_even(i_d):
    global flag
    print('Question:  ' + str(rand_list[i_d]))
    answer = input('Your answer: ')
    if answer == 'yes':
        print('Correct!')
        flag = True
        return flag
    elif answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        flag = False
        return flag
    else:
        print('Wrong answer.')
        flag = False
        return flag


def not_for_even(i_d):
    global flag
    print('Question:  ' + str(rand_list[i_d]))
    answer = input('Your answer: ')
    if answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        flag = False
        return flag
    elif answer == 'no':
        print('Correct!')
        flag = True
        return flag
    else:
        print('Wrong answer.')
        flag = False
        return flag


while flag is True:
    if order_list <= 2:
        if its_even(order_list) is True:
            for_even(order_list)
            order_list += 1
        else:
            not_for_even(order_list)
            order_list += 1
    elif order_list > 2:
        print(f'Congratulations, {name}!!!')
        break

if flag is False:
    print(f"Let's try again, {name}!")
