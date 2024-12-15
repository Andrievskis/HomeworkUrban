from lesson_07 import list_

my_dict = {"Anna": 1998, "Tina": 2000, "Pit": 1999}
print("Dict:", my_dict)
print(my_dict["Tina"])
print("Not existing value:", my_dict.get("Nina"))
my_dict.update({"Luna": 2002,
                "Tim": 1997})
d = my_dict.pop("Anna")
print("Deleted value:", d)
print("Modified dictionary:", my_dict)

my_set = {1, 1, 2, 3.34, 3.34, 4, "a", "a", "c", "cat", "cat"}
print("Set:", my_set)
print(my_set.add(8))
print(my_set.add("Y"))
print(my_set.discard("cat"))
print("Modified set:", my_set)


