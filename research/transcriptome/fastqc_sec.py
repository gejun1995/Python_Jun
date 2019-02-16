

a=['L','R']
b=["1P","1U","2P","2U"]
for part in a:
    for i in range(1, 4):
        for last in b:
            print('Cd_'+ part + str(i) + "_" + last +".fq ", end='')
print("\n")

a=['L','R']
b=["1P","1U","2P","2U"]
for part in a:
    for i in range(1, 4):
        for last in b:
            print('Ck_'+ part + str(i) + "_" + last +".fq ", end='')
print("\n")

a=['R']
b=["1P","1U","2P","2U"]
for part in a:
    for i in range(1, 4):
        for last in b:
            print('Cu_'+ part + str(i) + "_" + last +".fq ", end='')
print("\n")


a=['R']
b=["1P","1U","2P","2U"]
for part in a:
    for i in range(1, 4):
        for last in b:
            print('Pb_'+ part + str(i) + "_" + last +".fq ", end='')
print("\n")


a=['R']
b=["1P","1U","2P","2U"]
for part in a:
    for i in range(1, 4):
        for last in b:
            print('Zn_'+ part + str(i) + "_" + last +".fq ", end='')
print("\n")