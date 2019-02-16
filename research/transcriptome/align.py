
elements = ["Cd","Ck","Cu","Pb","Zn"]
for element in elements:
    if element =="Cd":
        a = ['L', 'R']
    if element =="Ck":
        a = ['L', 'R']
    if element =="Cu":
        a = ['R']
    if element =="Pb":
        a = ['R']
    if element =="Zn":
        a = ['R']
    for part in a:
        for i in range(1, 4):
            cd_in1 = element + '_' + part + str(i) + "_1P.fq"
            cd_in2= element + '_' + part + str(i) + "_2P.fq"
            cd_out = element + '_' + part + str(i)
            full = 'align_and_estimate_abundance.pl --transcripts /mnt/e/JunGe/TR/trinity/total/trinity_out_dir/Trinity.fasta --seqType fq --left ' + cd_in1 + ' --right ' + cd_in2 + ' --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir rsem_outdir_' + cd_out + ' --thread_count 3 &'
            print(full)