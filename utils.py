import json
import math

from flask import current_app


def get_dict_from_tuple(caption_tuple, data_tuple):
    """
    Получаем из кортежа словарь в качестве ключей передаем кортеж названий
    """
    dictionary = dict(zip(caption_tuple, data_tuple))
    return dictionary


def get_list_of_dict_from_tuple(caption_tuple, cursor):
    """
    Получаем список словарей в качестве ключей передаем кортеж названий
    """
    data_list = []
    for row in cursor:
        data_list.append(get_dict_from_tuple(caption_tuple, row))
    return data_list



def find_actors_cowokers(cursor, actor1, actor2, count):
    """
    Находим актеров сыгравших с заданными более count раз
    """

    actors = []
    for row in cursor:
        for actor in row[0].split(', '):
            if (not (actor in actors)) and (actor != actor1) and (actor != actor2):
                actors.append(actor)
    actors_dictionary = {actor: 0 for actor in actors}
    for row in cursor:
        for actor in actors_dictionary.keys():
            if actor in row[0]:
                actors_dictionary[actor] += 1 * row[1]
    actors = []
    for key, value in actors_dictionary.items():
        if value > count:
            actors.append(key)
    return actors


def get_page_counts(movies_count):
    """
    Разбиваем результат поиска по страничкам в каждой  'COUNT_ON_PAGE' штук (переменная в config)
    """
    page_count = math.ceil(movies_count / current_app.config.get('COUNT_ON_PAGE'))
    page_count_list = range(1, page_count + 1)
    return page_count_list
