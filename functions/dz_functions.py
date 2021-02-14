#!/usr/bin/env python
# coding: utf-8

# # Домашнее задание к лекции "Функции"

# In[ ]:


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}


def current_shelves(dirs):
    return ", ".join(list(dirs.keys()))


# ## Задание 1

# ### Пункт 1. Пользователь по команде "p" может узнать владельца документа по его номеру

# In[ ]:


def doc_owner(docs):
    doc_number = input("Введите номер документа: ")
    for value in docs:
        if value["number"] == doc_number:
            return f"Владелец документа: {value['name']}"
    return "Документ не найден в базе"


# ### Пункт 2. Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится

# In[ ]:


def shelf_number(dirs):
    doc_number = input("Введите номер документа: ")
    for key, value in dirs.items():
        if doc_number in value:
            return f"Документ хранится на полке: {key}"
    return "Документ не найден в базе"


# ### Пункт 3. Пользователь по команде "l" может увидеть полную информацию по всем документам

# In[ ]:


def shelf_number_l(dirs, shelf_number_input):
    for key, value in dirs.items():
        if shelf_number_input in value:
            return f"{key}"


def full_info(docs, dirs):
    full_list = []
    for value_doc in docs:
        item = f"№: {value_doc['number']}, тип: {value_doc['type']}, Владелец: {value_doc['name']}, полка хранения: {shelf_number_l(dirs, value_doc['number'])}"
        full_list.append(item)
    return "\n".join(full_list)


# ### Пункт 4. Пользователь по команде "ads" может добавить новую полку

# In[ ]:


def shelf_add(dirs):
    shelf_number = input("Введите номер полки: ")
    if shelf_number in dirs:
        return f"Такая полка уже существует. Текущий перечень полок: { current_shelves(dirs)}"
    for key in dirs:
        dirs[shelf_number] = []
        return f"Полка добавлена. Текущий перечень полок: {current_shelves(dirs)}"


# ### Пункт 5. Пользователь по команде "ds" может удалить существующую полку из данных (только если она пустая)

# In[ ]:


def shelf_del(dirs):
    shelf_number = input("Введите номер полки: ")
    if shelf_number in dirs:
        if dirs[shelf_number]:
            return f"На полке есть документ(ы), удалите их перед удалением полки. Текущий перечень полок: {current_shelves(dirs)}"
        else:
            del dirs[shelf_number]
            return f"Полка удалена. Текущий перечень полок: {current_shelves(dirs)}"
    return f"Такой полки не существует. Текущий перечень полок: {current_shelves(dirs)}"


# ## Задание 2 (необязательное)

# ### Пункт 1. Пользователь по команде "ad" может добавить новый документ в данные

# In[ ]:


def doc_ad(docs, dirs):
    doc_number = input("Введите номер документа: ")
    for value in docs:
        if doc_number == value["number"]:
            return "Такой документ уже существует."
    doc_type = input("Введите тип документа: ")
    doc_owner = input("Введите владельца документа: ")
    for value in docs:
        if doc_owner == value["name"] and doc_type == value["type"]:
            return f"У {doc_owner} уже есть документ такого типа."
    shelf_number = input("Введите полку для хранения: ")
    if shelf_number not in dirs.keys():
        return f"Такой полки не существует.\nДобавьте полку командой as.\nТекущий список документов:\n{full_info(docs, dirs)}"
    new_file = {}
    new_file["type"] = doc_type
    new_file["number"] = doc_number
    new_file["name"] = doc_owner
    docs.append(new_file)
    dirs[shelf_number].append(doc_number)
    return f"Документ добавлен.\nТекущий список документов:\n{full_info(docs, dirs)}"
# print(doc_ad(documents, directories))


# ### Пункт 2. Пользователь по команде "d" может удалить документ из данных

# In[ ]:


import copy


def doc_del(docs, dirs):
    doc_number = input("Введите номер документа: ")
    docs_copy = copy.deepcopy(docs)
    # print(docs_copy)
    for value in docs_copy:
        if doc_number == value["number"]:
            docs.remove(value)
            return (
                f"Документ удален.\nТекущий список документов:\n{full_info(docs, dirs)}"
            )
    return f"Документ не найден в базе.\nТекущий список документов:\n{full_info(docs, dirs)}"


# ### Пункт 3. Пользователь по команде "m" может переместить документ с полки на полку

# In[ ]:


def shelf_move(docs, dirs):
    doc_number = input("Введите номер документа: ")
    new_shelf_number = input("Введите номер полки: ")
    dirs_copy = copy.deepcopy(dirs)
    if new_shelf_number in dirs:
        for key, value in dirs_copy.items():
            if doc_number in dirs[key]:
                if key != new_shelf_number:
                    dirs[key].remove(doc_number)
                    dirs[new_shelf_number].append(doc_number)
                    dirs_copy = dirs
                    return f"Документ перемещен.\nТекущий список документов:\n{full_info(docs, dirs)}"
                return f"Документ уже на полке {new_shelf_number}.\nТекущий список документов:\n{full_info(docs, dirs)}"
        return f"Документ не найден в базе.\nТекущий список документов:\n{full_info(docs, dirs)}"
    return f"Такой полки не существует. Текущий перечень полок: {current_shelves(dirs)}"


# #### While cycle for commads and execution

# In[ ]:


# Добавить input из функций в main

def main(docs, dirs):
    while True:
        command = input("Введите команду: ")
        if command == "p":
            print(doc_owner(docs))
        elif command == "s":
            print(shelf_number(dirs))
        elif command == "l":
            print(full_info(docs, dirs))
        elif command == "ads":
            print(shelf_add(dirs))
        elif command == "ds":
            print(shelf_del(dirs))
        elif command == "ad":
            print(doc_ad(docs, dirs))
        elif command == "d":
            print(doc_del(docs, dirs))
        elif command == "m":
            print(shelf_move(docs, dirs))
        elif command == "w":
            print("Пока, пока!")
            break


main(documents, directories)


# In[ ]:




