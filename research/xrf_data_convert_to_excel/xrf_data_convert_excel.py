# coding=utf-8

import openpyxl as op
import re

"""
To convert XRF data into '.xlsx' format which was collected in SSRL.
Version 2.0
New features: 
1. Make read files in batches possible.
2. Some bug fixed.
By Jun Ge
Updated 8/20/2018
"""


# Convert numeric columns to alphabet columns.
def num_to_char(index):
    if index < 1:
        raise ValueError("Index is too small")
    result = ""
    while True:
        if index > 26:
            index, r = divmod(index - 1, 26)
            result = chr(r + ord('A')) + result
        else:
            return chr(index + ord('A') - 1) + result


# Read files in batches.
file_list = []
element_column_1_dic = {}
element_column_2_dic = {}
while True:
    filename_temp = input('\nPlease enter the filename without ".xlsx" in turn.\nEnter only "q" to start. ')
    if filename_temp == 'q':
        break
    filename = filename_temp + '.xlsx'
    file_list.append(filename)
    element_column_1_dic[str(filename)] = input('Please enter the column num that element starts in row 5. ')
    element_column_2_dic[str(filename)] = input('Please enter the column num that element starts in row 23. ')

# Main part.
for file in file_list:
    # Read data and mark the active page as 'origin'.
    wb = op.load_workbook(file)
    origin = wb.active
    print("\n" + str(file) + " loads successfully.")

    # Read the num of target rows and columns, and record them as row, col.
    row = origin.cell(row=1, column=1).value
    col = origin.cell(row=2, column=1).value
    row = re.findall("\d+", row)[0]
    col = re.findall("\d+", col)[0]
    print('The number of target row is ' + str(row))
    print('The number of target column is ' + str(col))

    # Detect element types and store them in element[].
    element = []
    num = 0
    column = int(element_column_1_dic[str(filename)])  # the column of element starts
    item = ''
    flag = True
    while flag:
        element.append(origin.cell(row=5, column=column).value)
        if element[num] == 'TIME':
            flag = False
        else:
            num += 1
            column += 1
            item += str(element[num - 1]) + ' '
    temp = 0
    element_column_2 = int(element_column_2_dic[filename])
    for b in range(element_column_2, 9 + num):
        origin.cell(row=22, column=b).value = element[temp]
        temp = temp + 1
    print("The detected items are: " + str(item))
    print("Total " + str(num) + " items")
    print("Data is converting...")

    # Sheet creating.
    for i in range(0, num):
        temp = 'ws' + str(i)
        temp = wb.create_sheet(element[i], i + 1)

        # Copy the original data to the new sheet.
        sheets = wb.get_sheet_names()
        sheet = sheets[i + 1]
        item = wb.get_sheet_by_name(sheet)
        a = 1
        b = 23
        flag = True
        while flag:
            item.cell(row=a, column=1).value = origin.cell(row=b, column=(element_column_2 + i)).value
            if origin.cell(row=(b + 1), column=(element_column_2 + i)).value is None:
                flag = False
            else:
                a = a + 1
                b = b + 1

        # Calculating for the new sheet.
        i = int(row) + 1
        j = int(col) + 2
        for a in range(1, int(i)):
            for b in range(2, int(j)):
                c = num_to_char(b - 1)
                d = a
                e = '=INDIRECT("a"&ROW(' + str(c) + str(d) + ')+(COLUMN(' + str(c) + str(d) + ')-1)*' + str(row) + ')'
                item.cell(row=a, column=b).value = e

    # Save file.
    new_filename = 'new_' + str(file)
    wb.save(filename=new_filename)
    print("Data converts successfully with a new filename " + new_filename)

print("Finished.")
