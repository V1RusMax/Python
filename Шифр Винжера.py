#!/usr/bin/env python
# coding: utf-8

# # Шифр Винжера

# В коде реализован шифр Винжера- метод полиалфавитного шифрования буквенного текста с использованием ключевого слова ( в данном случае кода-ключа)
# Функция принимает на входе 4 аргумента:
# - text - текстовая строка исходного текста (зашифрованного или подаваемого для зашифровки)
# - key - ключ, состоящий из цифр
# - alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ' текстовая строка алфавита - по умолчанию английский
# - reverse=False переключение функции шифрации/дешифрации

# In[3]:


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    # тут не самый лучший выход, вместо того чтобы зациклить я просто умножаю алфавит на 10) когда-нибудь приджумаю
    # что-то лучше
    alphabet2 = alphabet*10
    # переменная криптограммы для хранения текста перегнанного в цифры
    cryptogramm = []
    # результат функции
    result = ""
    # делаю из ключа список для итерации
    key = [i for i in str(key)]
    # заполняю криптограмму ключом по длине моего десятикратного алфавита
    for i in range(len(alphabet2)):
        cryptogramm.append(str(key[i % len(key)]))
    # счётчик для определения индекса буквы в тексте
    counter = -1
    # перебираю текст
    for i in text:
        # без учёта пробелов
        if i!= " ":
            # Шифрация
            if reverse == False:
                counter += 1
                # ищу номер(индекс) буквы в алфавите
                index = alphabet.find(i.upper())
                # рассчитываю новый индекс - это индекс в алфавите + цифра изменения индекса для этой буквы из ключа
                newindex = int(index) + int(cryptogramm[counter])
                # записываю в результат букву i с новым индексом
                result += alphabet2[newindex]
            # Дешифрация
            if reverse == True:
                counter += 1
                index = alphabet.find(i.upper())
                # тут оличие только в том, что я отнимаю индекс по ключу- обратный процесс
                newindex = int(index) - int(cryptogramm[counter])
                result += alphabet2[newindex]  
    # возвращаю результат
    return result


# ## дешифровка

# In[5]:


my_text = "UUNEFWKXKVUEECMDVLPRUQQYCYTIHWUKPZ"
my_key = 26101986
print(jarriquez_encryption(my_text, my_key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=True))


# In[10]:


my_text = "БНБШЙЭШФДЖМТФЫЪЛМЧУИГЧЪФП"
my_key = 26101986
my_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print(jarriquez_encryption(my_text, my_key, my_alphabet, reverse=True))


# ## шифрование

# In[15]:


my_text = "Я Зашифровал тут текст и вот он"
my_key = 26101986
my_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print(jarriquez_encryption(my_text, my_key, my_alphabet, reverse=False))


# # Расшифровка перебором

# - Исходный текст - ФЦХИВЬКЧУПДДПРИЛРЦРУЮКФЙМФХЙДТФСРНЗСБКСГХЦОГНТКРКВОЯГПАТЛТВЦЮНСЕПДСЛХППЙ
# - Алфавит - АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
# - Известно, что в тексте есть слова "люблю" и "код"
# - Ключ - значение не более шестизначного
# - Необходимо расшифровать текст и вывести ключ

# In[18]:


my_text = "ФЦХИВЬКЧУПДДПРИЛРЦРУЮКФЙМФХЙДТФСРНЗСБКСГХЦОГНТКРКВОЯГПАТЛТВЦЮНСЕПДСЛХППЙ"
my_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# In[19]:


for i in range(1, 999999):
    kerogaz = jarriquez_encryption(my_text, i, alphabet=my_alphabet, reverse=True)
    if "ЛЮБЛЮ" in kerogaz and "КОД" in kerogaz:
        print(kerogaz)
        print(i)


# In[ ]:




