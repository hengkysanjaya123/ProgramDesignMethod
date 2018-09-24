def is_member(x,a):
    for i in a:
        if(x == i):
            return True
    return False

print(is_member(1, ["abc", "test2", 1]))
