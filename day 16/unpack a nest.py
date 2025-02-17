# Unpack A Nest

nested_list = [[12, 34, 56, 67], [34, 68, 78]]

new_list = []

for i in nested_list:
    for j in i:
        if j in [34,67,78]:
            if j not in  new_list:
                new_list.append(j)

print(new_list)