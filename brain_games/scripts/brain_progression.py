#!/usr/bin/env python3
import random
import prompt


def main():
    pass


order_list = 0
flag = True
name = prompt.string('''Welcome to the Brain Games!
May I have your name?   ''')    # Приглашение к вводу имени
print('What is the result of the expression?')





def question(search_value):
    list_num = [i for i in range(1, random.randint(15, 30), random.randint(1, 4))]
    index_search_value = [random.randrange(1, len(list_num), 1) for i in range(3)]
    template_quest = list_num[:]; template_quest.pop(index_search_value[search_value]); template_quest.insert(index_search_value[search_value], '..')
    global flag
    print('Question:  ' + ", ".join(str(j) for j in template_quest))
    answer = input('Your answer: ')
    if answer == str(list_num[index_search_value[search_value]]):
        print('Correct!')
        flag = True
        return flag
    elif answer != str(list_num[index_search_value[search_value]]):
        print(f'{answer} is wrong answer ;(. Correct answer was {str(list_num[index_search_value[search_value]])}.')
        flag = False
        return flag
    else:
        print('Wrong answer.')
        flag = False
        return flag


while flag is True:
    if order_list <= 2:
        question(order_list)
        order_list += 1
    elif order_list > 2:
        print(f'Congratulations, {name}!!!')
        break

if flag is False:
    print(f"Let's try again, {name}!")
