def maps(listString):
    data = []
    for i in listString:
        data.append(len(i))

    return data

print(maps(["abc", "test", "jklasdf"]))
