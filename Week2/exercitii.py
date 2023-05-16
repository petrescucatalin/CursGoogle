# my_tuple = (1, 10, 100)
# t2 = my_tuple * 3
# print(len(t2))

# x = 10
# while x > 1:
#     x -= 1
#     continue
#     print(x)

# x = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "a": 4,
#     "d": 5
# }
#
# print(x["a"])

# item = 1
# lista = [1,2,3]
# for x, y in enumerate(lista):
#     item *= x
#     print(lista[y+1])
#     break

# my_var = ["a", "b", {"x": 1, "z": {"key": 30}, "w": 2}, 10]
# print(my_var[2]["z"]["key"])


# x = ["ab", "cd", "ed"]
# for i in x:
#     i.title()
#     print (x)

lista1 = list(set([1,3,2,3,4,5,6]))
del lista1[1:5]
print(lista1)
