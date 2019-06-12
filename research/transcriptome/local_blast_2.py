import os
import re

gene_name = "AtHMA5"
e_value = "1e-1"

print(
    "/mnt/f/software/ncbi-blast-2.9.0+/bin/blastn -query /mnt/f/gene/{0}.fasta -out /mnt/f/TR_1/local_blast/unigene/{0}_local_blast_top10.txt -db /mnt/f/TR_1/makeblastdb/unigene/ntdb -num_threads 4 -max_target_seqs 10 -outfmt 6 -evalue {1}".format(
        gene_name, e_value))
print(
    "/mnt/f/software/ncbi-blast-2.9.0+/bin/blastn -query /mnt/f/gene/{0}.fasta -out /mnt/f/TR_1/local_blast/transcriptsWithclusterTags.fa/{0}_local_blast_top10.txt -db /mnt/f/TR_1/makeblastdb/transcriptsWithclusterTags.fa/ntdb -num_threads 4 -max_target_seqs 10 -outfmt 6 -evalue {1}".format(
        gene_name, e_value))
print(
    "/mnt/f/software/ncbi-blast-2.9.0+/bin/blastn -query /mnt/f/gene/{0}.fasta -out /mnt/f/TR_2/local_blast/{0}_local_blast_top10.txt -db /mnt/f/TR_2/makeblastdb/ntdb -num_threads 4 -max_target_seqs 10 -outfmt 6 -evalue {1}".format(
        gene_name, e_value))
