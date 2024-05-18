

#Решение задачи 1: "Часть от целого"
sentence = "Сейчас на Земле появился новый вид роботов. Раньше их называли „железной оравой “, но это не очень точное определение"
first_sentence = sentence[:sentence.index('.') + 1]
print(first_sentence)


#Решение задачи 2: "Палиндром"
word = "радар"
reversed_word = word[::-1]
print(reversed_word)

# Проверка для слова "норма"
word2 = "норма"
reversed_word2 = word2[::-1]
print(reversed_word2)


#Решение задачи 3: "Равные части"
word = "кенгуру"
half_length = len(word) // 2
swapped_word = word[half_length:] + word[:half_length]
print(swapped_word)


#Решение задачи 4: "Четные и нечетные"
word = "нейропрограммирование"
even_chars = word[::2]
odd_chars = word[1::2]
print(even_chars, odd_chars)


#Решение задачи 5: "Обратный порядок"
word = "нейропластичность"
reversed_word = word[-2:0:-1]
print(reversed_word)
