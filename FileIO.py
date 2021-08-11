"""
File's:
* open
* Read ->r, r+
* Write ->w, w+
* Append ->a, a+
* close

.dat
.raw
.csv ->,
.psv -> |
.tsv -> `     `
.xls
.xlsx
.log

.json -> dict
.xml
.yml

.txp
.pdf
**
"""

# fs = open(r"./test.txt", 'w')
import os
#
# fs = open(r"./test.txt", 'a')
# fs.write("Hello world! -> new\n\ttest tab line\n")
# fs.close()
#
# fs = open(r"./test.txt", 'r')
# # print(fs.readline())
# print(fs.readlines())
# fs.close()
#
#
# with open(r"./test.txt", 'r') as i_fs:
#     fs=open(r"./test_out.txt", 'w')
#     fs.close()
#     with open(r"./test_out.txt", 'a') as o_fs:
#         for line in i_fs.readlines():
#             line = line.replace("\t", "")
#             o_fs.write(line)
#
#         o_fs.close()
#     i_fs.close()

final_output = []
with open(r"./vaccination-metadata.csv",'r') as fs:
    n = 0
    header = []
    for row in fs.readlines():
        row = row.split(",")
        if n==0:
            header = row
            n += 1
            continue

        new_row = {}
        for i in range(len(header)-1):
            new_row[header[i]] = row[i]

        final_output.append(new_row)
    fs.close()

print(final_output)

