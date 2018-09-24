def generate_n_chars(n , c):
    data = ""
    for i in range(n):
        data += c
    return data

print(generate_n_chars(5, "x"))
