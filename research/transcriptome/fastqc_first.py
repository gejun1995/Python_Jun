import re

a = 'fastqc Ck_R1_1.fq Ck_R1_2.fq Ck_R2_1.fq Ck_R2_2.fq Ck_R3_1.fq Ck_R3_2.fq'
b=a.replace("Ck","Pb")
c=a.replace("Ck","Zn")
print(b)
print(c)