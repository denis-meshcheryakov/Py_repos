#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "quiz.py"
#
ls = [
    ("Какая версия языка сейчас актуальна?", "python3"),
    ("Какая кодировка используется в строках?", "utf8"),
    ("Какой оператор сравнения нужно использовать для работы с None и bool?", "is"),
    ("Сколько значений есть у bool?", "2"),
    ("Что будет есть случайно умножить None на число?", "ошибка"),
    ("Чему равно len('abc')?", "3"),
    ("Какой цикл чаще используется?", "for"),
    ("Можно ли назвать свою переменную False?", "нет"),
    ("Что будет результатом выражение 3 == 3.0?", "true"),
    ("Как форматировать строку?", ".format")
]
answers_counter = [0, 0]
for q, a in ls:
    print(q)
    answer = input().strip().lower()
    if answer in a:
        print("Ответ {} верен".format(a))
        answers_counter[0] += 1
        answers_counter[1] += 1
    else:
        print("неправильный ответ")
        answers_counter[0] += 1
print("\nДано ответов: {}, Верных ответов: {}".format(answers_counter[0], answers_counter[1]))
input()
