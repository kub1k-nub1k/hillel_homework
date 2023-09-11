def dict_handler(link_on_dict, key, default_value=None):
    try:
        value = link_on_dict[key]
    except KeyError:
        link_on_dict[key] = default_value
        value = default_value
    except TypeError:
        error_message = f"Ключ {key} не може бути використаний в словнику"
        print(error_message)
        value = default_value

    return value

# Приклади використання:


my_dict = {'a': 1, 'b': 2, 'c': 3}

# №1 ключ 'b' вже існує в словнику
# result = dict_handler(my_dict, 'b', 10)
# print(result)

# №2 ключ 'd' був доданий зі значенням 10
# result = dict_handler(my_dict, 'd', 10)
# print(result)

# №3 ключ 'key' є змінюваним типом данних то він не може бути ключем словника
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key = [1, 2, 3]
# result = dict_handler(my_dict, key, 10)
# print(result)
