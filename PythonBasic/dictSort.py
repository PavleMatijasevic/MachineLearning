my_dict = {'apple':3, 'banana':1, 'date':4, 'cherry':2}

sorted_by_keys = dict(sorted(my_dict.items()))
sorted_by_values = dict(sorted(my_dict.items(), key=lambda items:items[1]))

print("Sorted by keys: ")
for k, v in sorted_by_keys.items():
    print(f"{k}: {v}")

print("Sorted by values: ")
for k, v in sorted_by_values.items():
    print(f"{k}: {v}")


