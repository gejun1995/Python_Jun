gene = []
with open("chose.txt", 'r') as chose:
    for line in chose:
        line = line.strip("\n")
        gene.append(line)
print(gene)

gene_full = []
with open("all.txt", 'r') as all:
    for line in all:
        line_split = line.split("\t")
        if line_split[0] in gene:
            gene_full.append(line)
print(gene_full)

with open("result.txt", 'w') as result:
    for line in gene_full:
        result.write(line)
