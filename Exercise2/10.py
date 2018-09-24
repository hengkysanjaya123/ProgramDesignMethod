def find_longest_word(listWord):
    max = 0
    for i in listWord:
        if(len(i) > max):
            max = len(i)

    return max

print(find_longest_word(["test", "abc", ""]))
