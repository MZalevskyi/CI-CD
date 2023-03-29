import re

def words_sentences(filename):
    # відкриваємо файл для зчитування
    with open(filename, "r") as file:
        # зчитуємо вміст файлу
        text = file.read()

    # визначаємо розділювачі
    separators = [",", " ", ":", ";"]

    # замінюємо всі символи-розділювачі на пробіли
    for sep in separators:
        text = text.replace(sep, " ")

    # визначаємо символи, що закінчують речення
    end_of_sentences = ["\.", "\!", "\?", "\..."]

    # рахуємо кількість слів у тексті
    words = len(text.split())

    # рахуємо кількість речень у тексті
    sentences = sum([len(re.findall(eos, text)) for eos in end_of_sentences])

    # повертаємо результат у вигляді словника
    return {"words": words, "sentences": sentences}

# використання функції
result = words_sentences("Text.txt")

