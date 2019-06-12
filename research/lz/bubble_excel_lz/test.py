sheet_name_list = ["CKNS", "CKS", "HMNS", "HMS"]
position_name_list = ["Unplanted", "Bulk", "FR", "RS", "RP", "E"]
position_replica_dic = {"Unplanted": 3, "Bulk": 6, "FR": 6, "RS": 6, "RP": 6, "E": 6}
positioin_start_dic = {"Unplanted": 2, "Bulk": 5, "FR": 11, "RS": 17, "RP": 23, "E": 29}

filename = "test"
test="43545"
with open(filename, 'a') as f:
    f.write(test)
