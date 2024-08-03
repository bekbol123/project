def multiply_by_index(a):
    new = []
    for i in a:
        i *= a.index(i)
        new.append(i)
    return new
print(multiply_by_index([1,2,3,4,5]))


# aaa = [1,2,3,4,5]
# new = []
#
# for i in aaa:
#     i *= aaa.index(i)
#     new . append(i)
#
# print(new)