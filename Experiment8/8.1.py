#Write a program to remove the item present at index 4 and add
# it to the 2nd position and at the end of the list.

l=[54,44,27,79,91,41]
a=l.pop(4)
print("list after removing element at index 4",l)
l.insert(2,a)
print("list after inserting element at index 2",l)
l.append(a)
print("list after appending element at last",l)
