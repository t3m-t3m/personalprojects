import random


from english_words import english_words_set


class TableGenerator:

    indexes = list()
    keywords = list()
    dictionary = [word.upper() for word in english_words_set
                  if len(word) == 4]
    symbols = '!@#$%^&*()_-+=/.,><;:]}[{'

    string = ''
    string_memory = ''
    table_view = ''

    def __init__(self):
        self.generate_table()

    def generate_table(self):
        self.generate_indexes()
        self.generate_string()
        for i in range(0, 16):
            self.table_view = f'{self.table_view}{self.indexes[i]}    ' \
                         f'{self.string[i * 12:i * 12 + 12]}    ' \
                         f'{self.indexes[i + 16]}    ' \
                         f'{self.string[(i + 16) * 12:(i + 16) * 12 + 12]}\n'

    def generate_indexes(self):
        start_int = random.randint(0, 10000)
        for i in range(0, 32):
            self.indexes.append(f'{hex(start_int)}'.upper().replace('X', 'x'))
            start_int += 1

    def generate_string(self):
        while len(self.keywords) < 8:
            keyword = random.choice(self.dictionary)
            if keyword not in self.keywords:
                self.keywords.append(keyword)
        for i in range(0, 384):
            self.string += random.choice(self.symbols)
        for i in range(0, len(self.keywords)):
            current_symbol = random.randint(i * 48, (i + 1) * 48 - 5)
            self.string = self.string.replace(
                self.string[current_symbol:current_symbol + 4],
                self.keywords[i])
        self.string_memory = self.string

    def highlight_word(self, word):
        self.string = self.string_memory
        word_id = self.string.index(word)
        if word_id % 12 > 8:
            pass
        else:
            self.string = self.string_memory[:word_id] + \
                          f'\033[42m\033[37m{word}\033[49m\033[32m' + \
                          self.string_memory[word_id + len(word):]
            self.table_view = ''
            margin_left = 0
            margin_right = 0
            margin_left_true = 1
            margin_right_overall = 0
            if word_id in range(16 * 12):
                margin_right_overall = 20
                margin_left_true = 0
            for i in range(16):
                if word_id in range(i * 12, i * 12 + 12):
                    bl = i * 12  # border left
                    blr = i * 12 + 32  # border left-right
                    br = (i + 16) * 12 + 20  # border right
                    brr = (i + 16) * 12 + 32  # border right-right
                    self.table_view = f'{self.table_view}{self.indexes[i]}' \
                                      f'    ' \
                                      f'{self.string[bl:blr]}' \
                                      f'    ' \
                                      f'{self.indexes[i + 16]}' \
                                      f'    ' \
                                      f'{self.string[br:brr]} \n'
                    margin_left = 20
                elif word_id in range((i + 16) * 12, (i + 16) * 12 + 12):
                    bl = i * 12  # border left
                    blr = i * 12 + 12  # border left-right
                    br = (i + 16) * 12  # border right
                    brr = (i + 16) * 12 + 32  # border right-right
                    self.table_view = f'{self.table_view}{self.indexes[i]}' \
                                      f'    ' \
                                      f'{self.string[bl:blr]}' \
                                      f'    ' \
                                      f'{self.indexes[i + 16]}' \
                                      f'    ' \
                                      f'{self.string[br:brr]} \n'
                    margin_right = 20
                else:
                    bl = i * 12 + margin_left
                    blr = i * 12 + 12 + margin_left
                    br = ((i + 16) * 12 + margin_left_true * margin_left +
                          margin_right + margin_right_overall)
                    brr = ((i + 16) * 12 + 12 + margin_left_true *
                           margin_left + margin_right + margin_right_overall)
                    self.table_view = f'{self.table_view}{self.indexes[i]}' \
                                      f'    ' \
                                      f'{self.string[bl:blr]}' \
                                      f'    ' \
                                      f'{self.indexes[i + 16]}' \
                                      f'    ' \
                                      f'{self.string[br:brr]} \n'
