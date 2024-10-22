class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = list(*file_name)

    def get_all_words(self):  # метод, который возвращает словарь следующего вида:
        # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        all_words = {}
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                for p in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if p in line:
                        line = line.replace(p, '')
                line = line.replace(' - ', ' ')
                line.split()
                words.extend(line.split())
        all_words[file_name] = words
        return all_words

    def find(self,
             word):  # Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
        t = {}
        for name, words in self.get_all_words().items():
            if word in words:
                t[name] = words.index(word.lower()) + 1
            return t

    def count(self, word):
        t = {}
        for name, words in self.get_all_words().items():
            t[name] = words.count(word.lower())
        return t


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
