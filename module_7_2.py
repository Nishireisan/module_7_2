def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    k = 1
    strings_positions = {}
    for i in strings:
        h_tuple = (k, file.tell())
        file.write(f'{i}\n')
        strings_positions.update({f'{h_tuple}': i})
        k += 1
    file.seek(0)
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
