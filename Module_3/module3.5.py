def single_root_words(root_word, *other_words):
    same_words = []
    #root_word = root_word.lower()
    for words in other_words:
        #if words.lower() in root_word or root_word in words.lower():
        if (root_word.lower().count(words.lower())
                or words.lower().count(root_word.lower())):
            same_words.append(words)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))



