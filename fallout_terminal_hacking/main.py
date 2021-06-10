import os
import keyboard


from table_generator import TableGenerator
from time import sleep


def hat(tries_left):
    print("\033[32m\033[1m Добро пожаловать в сеть \"РОБКО Индастриз(ТМ)\"")
    print("\033[32m Требуется пароль\n")
    print("\033[32m Осталось попыток  ", end="")
    for i in range(0, tries_left):
        print("\033[42m  \033[0m ", end="")
    print(end="\n\n")


def main():
    table_generator = TableGenerator()
    tries_left = 4
    word = None

    os.system("gnome-terminal --tab")
    os.system("clear")
    hat(tries_left)
    print("\033[32m\033[1m")
    print(table_generator.table_view)

    while True:
        if keyboard.is_pressed('tab'):
            table_generator.highlight_next()
            os.system("clear")
            hat(tries_left)
            print("\033[32m\033[1m")
            print(table_generator.table_view)
            os.system('aplay ./res/sounds/ui_terminal_charscroll_lp.wav')
            sleep(0.2)
        elif keyboard.is_pressed('up'):
            table_generator.highlight_previous()
            os.system("clear")
            hat(tries_left)
            print("\033[32m\033[1m")
            print(table_generator.table_view)
            os.system('aplay ./res/sounds/ui_terminal_charscroll_lp.wav')
            sleep(0.2)
        elif keyboard.is_pressed('down'):
            table_generator.highlight_next()
            os.system("clear")
            hat(tries_left)
            print("\033[32m\033[1m")
            print(table_generator.table_view)
            os.system('aplay ./res/sounds/ui_terminal_charscroll_lp.wav')
            sleep(0.2)


if __name__ == '__main__':
    main()
