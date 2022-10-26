#!/usr/bin/env python3
import prompt
from cli import welcome_user
def main():
    print('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()

name = prompt.string('May I have your name?') #Приглашение пользлвателя к вводу имени
welcome_user(name) #Вызов функции реализующей приветствие с пользователем
