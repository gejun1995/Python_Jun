
# -*- coding:utf8 -*-
import re

cluster = []

with open("transcriptsWithclusterTags.fa", encoding="utf8") as file:
    file_content = file.read()
    pattern = re.compile(r'Cluster-\w*.\w*i\d')
    cluster = pattern.findall(file_content)

cluster = list(set(cluster))
print(cluster)
print(len(cluster))
with open('corset_cluster.txt', 'w') as file_write:
    for item in cluster:
        file_write.write(item + "\n")