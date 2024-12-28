class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                line.replace("[',', '.', '=', '!', '?', ';', ':', ' - ' ]", '')
                words = line.split()
                all_words[file_name] = words
                return all_words

    def find(self, word):
        find_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_word[name] = words.index(word.lower()) + 1
        return find_word

    def count(self, word):
        find_count = {}
        for name, words in self.get_all_words().items():
            find_count[name] = words.count(word.lower())
        return find_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
