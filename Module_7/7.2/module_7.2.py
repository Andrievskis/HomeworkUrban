def custom_write(file_name, strings):
    strings_positions = {}
    number_string = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        a = file.tell()
        file.write(f'{str(string)} \n')
        strings_positions.update({(number_string, a): string})
        number_string += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
