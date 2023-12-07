dic={'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
'july': 54, 'Aug': 44, 'Sept': 54} 

new_list=list()

for i in dic.values():
    if i not in new_list:
        new_list.append(i)
print(new_list)