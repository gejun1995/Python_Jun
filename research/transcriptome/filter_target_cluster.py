# -*- coding:utf8 -*-
import re
import openpyxl as op

filename = 'filted_DE _test.xlsx'
wb = op.load_workbook(filename)
sheet = wb.active



cluster_target_ID = []

i = 1
while True:
    a = str(sheet.cell(row=i, column=1).value)
    if a is None:
        break
    cluster_target_ID.append(a)
    i = i + 1
print(cluster_target_ID)

cluster_total = []
cluster_seq = []

with open("transcriptsWithclusterTags.fa", encoding="utf8") as file:
    file_content = file.read()

    pattern = re.compile(r'Cluster-\w*.\w*[ATGC]*')
    cluster_total = pattern.findall(file_content)

    for cluster_total_item in cluster_total:
        pattern = re.compile(r'Cluster-\w*.\w*g\d')
        cluster_total_ID = pattern.findall(cluster_total_item)

        if cluster_total_ID in cluster_target_ID:
            pattern_seq = re.compile(r'[ATGC]*')
            cluster_seq = pattern_seq.findall(cluster_total_item)

            with open('new_transcriptsWithclusterTags.fa.txt', 'w') as file_write:
                file_write.write(">" + str(cluster_total_ID) + "\n")
                file_write.write(str(cluster_seq) + "\n")
