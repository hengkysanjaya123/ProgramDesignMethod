def countOccur(stringValue):
    count = {}

    for character in stringValue:
        count.setdefault(character, 0)
        count[character] = count[character] +1

    return count


print(countOccur("I do not know what I am doing."))
