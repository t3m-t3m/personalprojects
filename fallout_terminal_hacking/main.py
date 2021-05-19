import os


from table_generator import TableGenerator


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
    while 1:
        os.system("clear")
        hat(tries_left)
        print("\033[32m\033[1m")
        print(table_generator.table_view, sep=' ')
        word = input().upper()
        table_generator.highlight_word(word)


if __name__ == '__main__':
    main()
