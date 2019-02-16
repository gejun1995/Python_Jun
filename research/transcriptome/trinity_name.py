elements = ["Cd", "Ck", "Cu", "Pb", "Zn"]
for element in elements:
    if element == "Cd":
        a = ['L', 'R']
    if element == "Ck":
        a = ['L', 'R']
    if element == "Cu":
        a = ['R']
    if element == "Pb":
        a = ['R']
    if element == "Zn":
        a = ['R']
    for part in a:
        for i in range(1, 4):
            dir = 'trinity_' + element + '_' + part + str(i) + ".fq "
            left = element + '_' + part + str(i) + "_1P.fq "
            right = element + '_' + part + str(i) + "_2P.fq "
            final = "Trinity --seqType fq --max_memory 16G --CPU 16 --min_kmer_cov 2 --output /mnt/f/TR_1/trinity_out_dir/" + dir + " --left " + left + " --right " + right
            print(final)
