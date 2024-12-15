data_structure = [[1, 2, 3], {'a':4, 'b':5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    numbers = 0
    strings = 0

    def sum(data):
        nonlocal numbers, strings
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                sum(item)
        elif isinstance(data, dict):
            for value in data.values():
                sum(value)
            for key in data.keys():
                sum(key)
        elif isinstance(data, int) or isinstance(data, str):
            if isinstance(data, int):
                numbers += data
            elif isinstance(data, str):
                strings += len(data)

    sum(data_structure)
    return numbers + strings
print(calculate_structure_sum(data_structure))





