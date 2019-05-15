import re

all_cluster = []
uni_cluster = []
trinity_cluster = []

with open(
        r"F:\TR_1\P101SC16120056-01-B1-4_result\P101SC16120056-01-B1-4_results\3.TranscriptomeAssembly\3.1.AssembledTranscriptome\Trinity.fasta",
        encoding="utf8") as file:
    file_content = file.read()
    trinity_pattern = re.compile(r'c\w*\d')
    trinity_cluster = trinity_pattern.findall(file_content)

with open(
        r"F:\TR_1\P101SC16120056-01-B1-4_result\P101SC16120056-01-B1-4_results\3.TranscriptomeAssembly\3.1.AssembledTranscriptome\cluster_all.fasta",
        encoding="utf8") as file:
    file_content = file.read()
    all_pattern = re.compile(r'Cluster-\d*.\d*')
    all_cluster = all_pattern.findall(file_content)

with open(
        r"F:\TR_1\P101SC16120056-01-B1-4_result\P101SC16120056-01-B1-4_results\3.TranscriptomeAssembly\3.1.AssembledTranscriptome\unigene.fasta",
        encoding="utf8") as file:
    file_content = file.read()
    uni_pattern = re.compile(r'Cluster-\d*.\d*')
    uni_cluster = uni_pattern.findall(file_content)

alone_cluster = (set(all_cluster) | set(uni_cluster)) - (set(all_cluster) & set(uni_cluster))
both_cluster = set(all_cluster) & set(uni_cluster)
total_cluster = set(all_cluster) | set(uni_cluster)
all_cluster_set = set(all_cluster)

with open('trinity_cluster.txt', 'w') as file_write:
    for item in trinity_cluster:
        file_write.write(item + "\n")

with open('all_cluster.txt', 'w') as file_write:
    for item in all_cluster:
        file_write.write(item + "\n")

with open('uni_cluster.txt', 'w') as file_write:
    for item in uni_cluster:
        file_write.write(item + "\n")

with open('alone_cluster.txt', 'w') as file_write:
    for item in alone_cluster:
        file_write.write(item + "\n")

with open('both_cluster.txt', 'w') as file_write:
    for item in both_cluster:
        file_write.write(item + "\n")

with open('total_cluster.txt', 'w') as file_write:
    for item in total_cluster:
        file_write.write(item + "\n")

with open('all_cluster_set.txt', 'w') as file_write:
    for item in all_cluster_set:
        file_write.write(item + "\n")