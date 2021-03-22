"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:

#>>> >>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
в теле функции или снаружи.

"""

def num_translate(num):

    dict_numb = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восель',
        'nine': 'девять',
        'ten': 'десять',
    }

    if num in dict_numb:
        return dict_numb[num]



print(num_translate('five'))

# При несуществующем ключе возвращает None, без get.
# Вопрос такой: в разборе Вы говорите, что лучше создавать словарь вне ф-ции. Тогда получается, что словарь надо
# создавать каждый раз перед использованием ф-ции, если мы хотим исп ф-ию в другом проекте? Так разве удобно?


