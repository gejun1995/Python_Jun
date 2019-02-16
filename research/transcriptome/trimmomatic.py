
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
            cd_in1 = '/mnt/f/TR_1/raw_data/' + element + '_' + part + str(i) + "_1" + ".fq "
            cd_in2 = '/mnt/f/TR_1/raw_data/' + element + '_'+ part + str(i) + "_2" + ".fq "
            cd_out = '/mnt/f/TR_1/clean_data/' + element + '_' + part + str(i) + ".fq "
            full = 'java -jar /home/jun/miniconda2/share/trimmomatic-0.38-1/trimmomatic.jar PE -threads 10 -phred33 ' + cd_in1 + ' ' + cd_in2 + ' -baseout ' + cd_out + ' ILLUMINACLIP:/home/jun/miniconda2/share/trimmomatic-0.38-1/adapters/novogene.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 HEADCROP:8 MINLEN:36'
            print(full)
