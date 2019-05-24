import re
import linecache

with open(r'F:\TR_3\Acc_Gene.fa', 'r') as acc_db:
    for (acc_db_num, acc_db_seq) in enumerate(acc_db):
        acc_db_seq = re.findall(r'[ATGCatgc]*', acc_db_seq)[0]
        acc_db_seq = acc_db_seq.upper()
        print("acc_db_seq is: " + str(acc_db_seq))
        print("acc_db_num is: " + str(acc_db_num))
        seq = "ATG"
        if seq in acc_db_seq:
            acc_db_ID = linecache.getline(r'F:\TR_3\new_Acc_Gene.fa', acc_db_num)
            acc_db_ID = re.findall(r'Ac\w*\d', acc_db_ID)[0]
            print("acc_db_ID is: " + acc_db_ID)
