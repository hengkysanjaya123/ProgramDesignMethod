def isPangram(stringValue):
    data = list("abcdefghijklmnopqrstuvwxyz ")
    array = [0 for i in range(0, len(data))]

    for i in stringValue.lower():
        idx = data.index(i)
        array[idx] = array[idx] + 1

    for i in array:
        if(i == 0):
            return False

    return True


print(isPangram("The quick brown fox jumps over the lazy "))




