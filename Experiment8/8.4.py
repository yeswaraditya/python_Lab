rollnum=[47,45,27,24,35,46,57,68]
sampleDict={'john':47,'emma':35,'kell':45}

for i in rollnum:
    if not i in sampleDict.values():
        rollnum.remove(i)
print("after removing unwanted elements from the list",rollnum)