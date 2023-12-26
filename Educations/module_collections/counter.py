from collections import Counter
import sys
import json
import csv


def count_files():
    """
    Вам доступен список files, содержащий названия различных файлов. Дополните приведенный ниже код, чтобы он вывел все
    расширения файлов, присутствующие в списке files, указав для каждого количество файлов с данным расширением.
    Расширения должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
    <расширение>: <количество файлов>
    Примечание. Начальная часть ответа выглядит так:
    csv: 5
    exe: 12
    ...
    """
    files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
             'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
             'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
             'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
             'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
             'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
             'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
             'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
             'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
             'forest.jpeg', 'python_for_pro8.mp4', 'discrepancy.exe', 'but-you.mp3',
             'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
             'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
             'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
    count_files_ = Counter([file[file.find(".")+1:] for file in files])
    sorted_count_files = sorted(count_files_.items(), key=lambda d: d[0])
    return [f'{el[0]}: {el[1]}' for el in sorted_count_files]
# print(*count_files(), sep="\n")


def count_occurrences(word: str, words: str):
    """
    Реализуйте функцию count_occurrences(), которая принимает два аргумента в следующем порядке:
    word — слово
    words — последовательность слов, разделенных пробелом
    Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный
    результат.
    Примечание 1. Функция должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
    Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию count_occurences(),
    но не код, вызывающий ее.
    """
    count_words = Counter(words.lower().split(" "))
    return count_words[word.lower()]


def shopping_list(string: str):
    """
    Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания
    количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур
    записывает в нижнем регистре через запятую.
    Напишите программу, которая выводит все товары из данного списка покупок, указывая для каждого его количество.
    Формат входных данных
    На вход программе подается последовательность товаров, разделенных запятой без пробелов.
    Формат выходных данных
    Программа должны вывести все введенные товары, указывая для каждого, сколько раз он встречается в данной
    последовательности. Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке,
    в следующем формате:
    <товар>: <количество>
    """
    count_shopping = Counter(string.split(','))
    sorted_shopping = sorted(count_shopping.items(), key=lambda d: d[0])
    return [f"{el[0]}: {el[1]}" for el in sorted_shopping]
# my_string = "лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви"
# my_string = "рубашка,футболка,футболка,брюки,футболка,рубашка,носки,рубашка"
# print(*shopping_list(my_string), sep="\n")


def course_cost(string: str):
    """
    Тимур живет в мире, в котором цена товара определяется как сумма Unicode кодов букв его названия. Буквенным
    обозначением данной валюты являются две заглавные латинские буквы UC. Например, ручка в его мире стоит:
    1088+1091+1095+1082+1072=5428UC
    Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания
    количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур
    записывает в нижнем регистре через запятую.
    Напишите программу, которая группирует одинаковые товары из данного списка покупок и определяет стоимость каждой
    группы.
    Формат входных данных
    На вход программе подается последовательность товаров, разделенных запятой без пробелов.
    Формат выходных данных
    Программа должна сгруппировать одинаковые товары, определить общую стоимость каждой группы и вывести полученный
    результат. Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем
    формате:
    <товар>: <цена за единицу товара> UC x <количество товаров в группе> = <общая стоимость группы> UC
    Примечание 1. Программа должна добавлять нужное количество пробелов, если название товара имеет меньшую длину,
    чем другие.
    Примечание 2. Получить Unicode код символа можно с помощью функции ord().
    """
    count_dict = Counter(string.split(","))
    max_length = max([len(el[0]) for el in count_dict.items()])
    text = ""
    for name, count in sorted(count_dict.items(), key=lambda x: x[0]):
        text += str(name)
        text += " " * (max_length - len(name)) + ": "
        price = sum([ord(letter) for letter in name if letter != " "])
        text += str(price) + " UC x " + str(count) + " = " + str(price * count) + " UC\n"

    return text[:-1]
# string1 = "лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви"
# string2 = "рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка"
# print(course_cost(string2))


def the_zen_of_python():
    """
    Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    ...
    Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество
    должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:
    <буква>: <количество>
    Примечание 1. Начальная часть ответа выглядит так:
    a: 53
    b: 21
    ...
    Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.
    Примечание 3. Программа должна игнорировать все небуквенные символы.
    """
    with open("pythonzen.txt") as file:
        count_letters = Counter(file.read().lower().strip(""))
        sorted_count_letters = sorted(filter(lambda x: x[0] in "abcdefghijklmnopqrstuvwxyz", count_letters.items()),
                                      key=lambda x: x[0])
        return list(map(lambda x: f"{x[0]}: {x[1]}", sorted_count_letters))
# print(*the_zen_of_python(), sep='\n')


def searching_for_words1(string: str):
    """
    Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
    последовательности.
    Формат входных данных
    На вход программе подается последовательность слов, разделенных пробелом.
    Формат выходных данных
    Программа должна определить наиболее часто встречаемое слово во введенной последовательности и вывести его в
    нижнем регистре.
    Примечание 1. Гарантируется, что искомое слово единственное.
    Примечание 2. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
    """
    counter_words = Counter(string.lower().split(' '))
    return counter_words.most_common(1)[0][0]
# string = "Арбуз Малина малина Арбуз клубника АрбуЗ Банан Малина вишня Черешня Вишня арбуз"
# print(searching_for_words1(string))


def searching_for_words2(string: str):
    """
    Дана последовательность слов. Напишите программу, которая выводит наименее часто встречаемое слово в этой
    последовательности. Если таких слов несколько, программа должна вывести их все.
    Формат входных данных
    На вход программе подается последовательность слов, разделенных пробелом.
    Формат выходных данных
    Программа должна определить наименее часто встречаемое слово во введенной последовательности и вывести его в
    нижнем регистре. Если таких слов несколько, программа должна вывести их все в лексикографическом порядке, в нижнем
    регистре, разделяя запятой и пробелом.
    Примечание 1. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
    """
    counter_words = Counter(string.lower().split(' '))
    min_count = min(counter_words.values())
    sorted_word = list(map(lambda x: x[0], sorted(filter(lambda x: x[1] == min_count, counter_words.most_common()),
                                                  key=lambda x: x[0])))
    return ", ".join(sorted_word)
# string_ = "Арбуз Малина Малина Арбуз Клубника арбуз банан малина вишня черешня вишня арбуЗ"
# print(searching_for_words2(string_))


def searching_for_words3(string: str):
    """
    Дана последовательность слов. Напишите программу, которая выводит наиболее часто встречаемое слово в этой
    последовательности. Если таких слов несколько, программа должна вывести то, которое больше в лексикографическом
    сравнении.
    Формат входных данных
    На вход программе подается последовательность слов, разделенных пробелом.
    Формат выходных данных
    Программа должна определить наиболее часто встречаемое слово во введенной строке и вывести его в нижнем регистре.
    Если таких слов несколько, программа должна вывести то, которое больше в лексикографическом сравнении, также в
    нижнем регистре.
    Примечание 1. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
    """
    counter_words = Counter(string.lower().split(' ')).most_common()
    max_ = max(counter_words, key=lambda x: x[1])[1]
    sorted_counter = sorted(filter(lambda x: x[1] == max_, counter_words), key=lambda x: x[0])
    return sorted_counter[-1][0]
# s = "арбуз банан клубника вишня малина"
# print(searching_for_words3(s))


def word_length_statistics(string: str):
    """
    Дана последовательность слов. Напишите программу, которая группирует слова из этой последовательности по их длине и
    определяет количество слов в каждой полученной группе.
    Формат входных данных
    На вход программе подается последовательность слов, разделенных пробелом.
    Формат выходных данных
    Программа должна сгруппировать слова из введенной последовательности по их длине и определить количество слов в
    каждой полученной группе. Каждую группу характеризуют два числа — длина слов в этой группе и количество слов в этой
    группе. Например, для группы {is, to, hi, no} это числа 2 и 4. Программа должна вывести данные о каждой группе,
    расположив их в порядке увеличения количества слов в них, каждые на отдельной строке, в следующем формате:
    Слов длины <длина слов в группе>: <количество слов в группе>
    Примечание 1. Если две разные группы имеют равное количество слов, то первой должна следовать та группа, слово
    которой в исходной последовательности встречается раньше.
    """
    counter_words = Counter([len(el) for el in string.lower().split(' ')]).most_common()
    sorted_words = sorted(counter_words, key=lambda x: x[1])
    return [f"Слов длины {el[0]}: {el[1]}" for el in sorted_words]
# s = "Любимой песни слог Знакомый ритм слов Панацея от всего"
# print(*word_length_statistics(s), sep='\n')


def second_student():
    """
    Дан список имен учеников и их оценок за экзамен. Напишите программу, которая определяет второго по счету ученика,
    имеющего самую низкую оценку.
    Формат входных данных
    На вход программе подается произвольное количество строк, в каждой из которых записаны имя очередного ученика и
    его оценка, разделенные пробелом.
    Формат выходных данных
    Программа должна определить второго по счету ученика, который имеет самую низкую оценку, и вывести его имя.
    Примечание 1. Гарантируется, что все ученики имеют различные имена и оценки.
    """
    list_students = sorted([el.rstrip().split(' ') for el in sys.stdin], key=lambda x: int(x[1]))
    return list_students[1][0]
# print(second_student())


def counter_with_dict():
    """Вам доступна переменная data, содержащая Counter словарь. Дополните приведенный ниже код, чтобы он добавил этому
    словарю два атрибута:
    min_values() — функция, которая возвращает список элементов, имеющих наименьшее значение
    max_values() — функция, которая возвращает список элементов, имеющих наибольшее значение
    Обе функции не должны принимать никаких аргументов.
    Примечание 1. Элементом словаря будем считать кортеж (ключ, значение).
    Примечание 2. Элементы словаря в возвращаемых функциями списках должны располагаться в своем исходном порядке.
    Примечание 3. Функции data.min_values() и data.max_values() должны учитывать содержимое словаря. Например, если в
    словарь data будет добавлена новая пара ключ-значение, то и в возвращаемых функциями списках данные ключ и значение
    должны присутствовать.
    Примечание 4. Программа ничего не должна выводить.
    """
    data = Counter(
        'aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
    data.__dict__['max_values'] = lambda: [el for el in data.items() if el[1] == max(data.values())]
    data.__dict__['min_values'] = lambda: [el for el in data.items() if el[1] == min(data.values())]
    print(data)
    print(data.max_values())
    print(data.min_values())
# counter_with_dict()


def here_we_do_again():
    """
    Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано
    измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом
    email пользователь менять не может, только имя:
    username,email,dtime
    rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
    busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
    ...
    Напишите программу, которая определяет, сколько раз пользователь менял имя. Программа должна вывести адреса
    электронных почт пользователей, указав для каждого соответствующее количество смененных имен. Почтовые ящики должны
    быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
    <адрес электронной почты>: <количество изменений имен>
    Примечание 1. Начальная часть ответа выглядит так:
    barbaraanderson@bk.ru: 3
    barbarabrown@rambler.ru: 3
    ...
    """
    with open("name_log.csv", encoding="UTF-8") as file:
        data = [row for row in csv.DictReader(file)]
    counter_info = Counter([el['email'] for el in data]).most_common()
    sorted_info = sorted(counter_info, key=lambda x: x[0])
    return list(map(lambda x: f'{x[0]}: {x[1]}', sorted_info))
# print(*here_we_do_again(), sep='\n')


def scrabble(symbols: str, word: str) -> bool:
    """
    Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
    symbols — набор символов
    word — слово
    Функция должна возвращать True, если из набора символов symbols можно составить слово word, или False в противном
    случае.
    Примечание 1. При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается
    их регистр.
    Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию scrabble(), но не код,
    вызывающий ее.
    """
    count_letters1 = Counter(symbols.lower())
    count_letters2 = Counter(word.lower())
    u = count_letters1 & count_letters2
    return u == count_letters2
# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# print(scrabble('begk', 'beegeek'))
# print(scrabble('beegeek', 'beegeek'))


def print_bar_chart(data: str or list, mark: str):
    """
    Реализуйте функцию print_bar_chart(), которая принимает два аргумента в следующем порядке:
    data — строка или список строк
    mark — одиночный символ
    Функция должна определять:
    сколько раз встречается каждый символ в строке, если data является строкой
    сколько раз встречается каждая строка в списке, если data является списком
    Затем функция должна выводить результат в виде столбчатой диаграммы, указывая каждый символ (строку) и его
    количество. Количество отображается как повторение символа mark соответствующее число раз, например, если mark='+',
    то количество, равное четырем, будет отображено как ++++. Символы (строки) в диаграмме должны быть расположены в
    порядке уменьшения количества, при равных количествах — в своем исходном порядке, каждая на отдельной строке, в
    следующем формате:
    <символ или строка> |<количество>
    Примечание 1. Обратите внимание на второй тест, функция должна добавлять нужное количество пробелов, если строка
    имеет меньшую длину, чем другие.
    Примечание 2. Программа должна учитывать регистр. То есть, например, строки Python и python считаются различными.
    Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_bar_chart(),
    но не код, вызывающий ее.
    """
    counter_symbols = Counter(data).most_common()
    max_length = max([len(el[0]) for el in counter_symbols])
    text = [f'{el[0]}{str(" ") * (max_length - len(el[0]) + 1) }|{el[1] * mark}' for el in counter_symbols]
    return print(*text, sep='\n')
# print_bar_chart('beegeek', '+')
# languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
# print_bar_chart(languages, '#')


def profit_calculation1():
    """
    Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год,
    разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. В каждом файле в
    первом столбце указывается название продукта, а в последующих — количество проданного продукта в килограммах за
    определенный месяц:
    продукт,январь,февраль,март
    Картофель,39,61,3
    Дайкон,51,96,83
    ...
    Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а значением —
    цена за килограмм в рублях:
    {
       "Картофель": 53,
       "Дайтон": 55,
    ...
    }
    Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.
    """
    # Получаю инфу о цене овощей
    with open('prices.json', encoding='UTF-8') as json_file:
        dict_price = json.load(json_file)

    # Получаю инфу о продажах
    counter_sales = Counter()
    for i in range(1, 5):
        filename = f'quarter{i}.csv'
        with open(filename, encoding='UTF-8') as csv_file:
            data_sales = csv.reader(csv_file)
            for row in list(data_sales)[1:]:
                counter_sales += Counter({row[0]: sum(map(int, row[1:]))})

    total = 0
    # Считаем заработок
    for product, kg in counter_sales.items():
        total += dict_price[product] * kg
    return total
# print(profit_calculation1())


def profit_calculation2():
    """
    Тимур продает книги по математике за 1—11 класс. У него есть список, в котором указаны все книги, имеющиеся в
    наличии. К Тимуру приходят n покупателей, называют номер класса, за который они хотят приобрести книгу, и сумму,
    которую они готовы заплатить, и если книга есть в наличии, Тимур ее продает.
    Напишите программу, которая вычисляет общую сумму денег, которую Тимур заработает на продаже книг.
    Формат входных данных
    На вход программе в первой строке подается последовательность чисел, разделенных пробелом, представляющих набор
    книг, которые имеются в наличии. Каждое число последовательности — книга за указанный класс, например,
    последовательность 1 1 4 представляет набор из двух книг за первый класс и одной книги за четвертый класс. Вторая
    строка содержит число n — количество покупателей. В последующих n строках вводятся два числа, разделенные пробелом,
    где первое число является номером класса, второе — суммой, предлагаемой покупателем.
    Формат выходных данных
    Программа должна вывести единственное число — общую сумму денег, которую заработал Тимур.
    Примечание. Рассмотрим первый тест. В первой строке указан список книг, которые есть в наличии:
    2 книги за 1-й класс
    1 книга за 11-й класс
    3 книги за 9-й класс
    2 книги за 5-й класс
    1 книга за 7-й класс
    В следующей строке указано число
    7 — количество покупателей. Последующие 7 строк содержат номер класса и некоторую сумму:
    первый покупатель приобретает книгу за 1-й класс за 300р
    второй покупатель приобретает книгу за 1-й класс за 250р
    третий покупатель приобретает книгу за 11-й класс за 400р
    книг за 1-й класс больше нет в наличии, поэтому покупка невозможна
    пятый покупатель приобретает книгу за 7-й класс за 200р
    шестой покупатель приобретает книгу за 9-й класс за 400р
    книг за 7-й класс больше нет в наличии, поэтому покупка невозможна
    Итого Тимур заработал 300+250+400+200+400=1550р.
    """
    # Записываем сколько книг в наличии
    in_stock = Counter(map(int, input().split(' ')))
    count_buyer = int(input())

    # Переменная для прибыли
    total = 0

    # Проходим по посетителям
    for buyer in range(count_buyer):
        class_, price = map(int, input().split(' '))
        book = Counter({class_: 1})  # Переменная для книги
        can_sales = book & in_stock  # Определяем есть ли книга в наличии
        if can_sales.total() != 0:
            total += price
            in_stock -= can_sales
    return total
print(profit_calculation2())
