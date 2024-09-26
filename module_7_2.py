def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a+', encoding='utf-8')
    num_str = 1
    for str_ in strings:
        strings_positions[(num_str, file.tell())] = str_
        file.write(str_ + '\n')
        num_str += 1
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

