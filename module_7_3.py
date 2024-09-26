class WordsFinder():
    def __init__(self, *files):
        self.file_names = files

    def get_all_words (self):
        all_words = dict()
        for name in self.file_names:
           with open(name, 'r', encoding='utf-8') as file:
               line=file.read().lower()
               for char in line:
                   if char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                       line=line.replace(char,' ')
               all_words[name] = list(line.split())
        return all_words

    def find(self, word):
        dict_return = dict()
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                dict_return[key] = value.index(word.lower())+1
        return dict_return

    def count(self, word):
        dict_return = dict()
        for key, value in self.get_all_words().items():
            dict_return[key] = value.count(word.lower())
        return dict_return

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#     'Mother Goose - Monday’s Child.txt','Rudyard Kipling - If.txt' )
# print(finder2.get_all_words())
# print(finder2.find('the'))
# print(finder2.count('the'))

