#!/usr/bin/env python3
import random
import prompt


def main():
    pass


name = prompt.string('''Welcome to the Brain Games!
May I have your name?   ''')    # Приглашение к вводу имени


order_list = 0
flag = True
numbers = '2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59'
numbers_list = numbers.split(', ')
numbers_list = [int(i) for i in numbers_list]
other_numb = [x for x in range(1, 61)]
index_search_value = [random.randrange(1, len(other_numb), 1) for i in range(3)]
print('Answer "yes" if given number is prime. Otherwise answer "no".')



def question(numb_list, other_numb, search_value):
    global flag
    print('Question:  ' + str(other_numb[index_search_value[search_value]]))
    answer = input('Your answer: ')
    if answer == 'yes' and other_numb[index_search_value[search_value]] in numb_list:
        print('Correct!')
        flag = True
        return flag
    elif answer == 'no' and other_numb[index_search_value[search_value]] not in numb_list:
        print('Correct!')
        flag = True
        return flag
    else:
        print('Wrong answer.')
        flag = False
        return flag


while flag is True:
    if order_list <= 2:
        if question(numbers_list, other_numb, order_list) is True:
            order_list += 1
    elif order_list > 2:
        print(f'Congratulations, {name}!!!')
        break

if flag is False:
    print(f"Let's try again, {name}!")
