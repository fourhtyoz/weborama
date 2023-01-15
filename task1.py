def build_dict_from_csv(file='table.csv'):
    """
    Функция обратаывает CSV и создает словарь {id: [cache]}.
    Возвращает словарь
    """
    # Обрабатывает CSV
    with open(file, 'r') as f:
        l = []
        next(f) # Пропускаем headers
        for line in f.readlines():
            l.append(line.strip().split(','))
    
    # Создает словарь {id: [cache]}
    d = {}
    for [cache, id] in l:
        if id not in d:
            d.setdefault(id, [])
            d[id].append(cache)
        else:
            d[id].append(cache)
    return d

def find_id_n_times(d, times=3):
    """
    Получает словарь, находит ID, которые встретились заданное кол-во раз. 
    Возвращает лист.
    """
    res = []
    for key in d:
        if len(d[key]) == 3:
            res.append(key)
    return res

def count_occurences(d):
    """
    Получает словарь, подсчитывает частоту повторений
    Возвращает лист
    """
    res = {}
    for key in d:
        a = len(d[key])
        if a not in res:
            res[a] = 1
        else:
            res[a] += 1
    return res

# Ответы
# Вывести те id, которые встречаются в файле только 3 раза
print(find_id_n_times(build_dict_from_csv()))

# Вывести частоту повторений
print(count_occurences(build_dict_from_csv()))