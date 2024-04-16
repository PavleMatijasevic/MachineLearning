def return_only_integer(list1):
    return [x for x in list1 if isinstance(x, int) and not isinstance(x, bool)]

print(return_only_integer([9,2,"space", "car", "lion", 16]))
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String", True, 3.3, 1]))

def society_name(names):
    secret_name = ''.join(sorted([name[0] for name in names]))
    return secret_name

print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", 'Newt', "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
