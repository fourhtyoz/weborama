# Uses a CSV file in ., parses it and returns a dict id: [cache]
def build_dict_from_csv(file='table.csv'):
    # Parse CSV
    with open(file, 'r') as f:
        l = []
        next(f)
        for line in f.readlines():
            l.append(line.strip().split(','))
    
    # Create a dict
    d = {}
    for [cache, id] in l:
        if id not in d:
            d.setdefault(id, [])
            d[id].append(cache)
        else:
            d[id].append(cache)
    return d

# Finds IDs that occurred 3 times
def find_id_times(d, times=3):
    res = []
    for key in d:
        if len(d[key]) == 3:
            res.append(key)
    return res

# Counts all ID occurences 
def count_occurences(d):
    res = {}
    for key in d:
        a = len(d[key])
        if a not in res:
            res[a] = 1
        else:
            res[a] += 1
    return res
