# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"В слове {word} последняя буква: {word[-1:]}\n")


# Вывести количество букв "а" в слове
word = 'Архангельск'
cymbol_to_count = 'а'
cymbols_in_word = word.lower().count(cymbol_to_count)
print(
    f'Количество букв "{cymbol_to_count}" в слове {word}: {cymbols_in_word}\n')


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюя'
vowels_sum = 0
for symbol in word:
    if symbol.lower() in vowels:
        vowels_sum += 1
print(
    f'Количество гласных букв в слове {word}: {vowels_sum}\n')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_quantity = sentence.count(' ') + 1
print(
    f"Количество слов в тексте: '{sentence}' - {words_quantity}\n")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f"Первые буквы в словах из: '{sentence}'")
[print(word[0]) for word in sentence.split()]
print()


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_num = len(sentence.split())
symbols_sum = sum([len(word) for word in sentence.split()])
avg_cymbols_in_sentence = symbols_sum // words_num
print(
    f"Средняя длина слова в предложении: '{sentence}' - {avg_cymbols_in_sentence}")
