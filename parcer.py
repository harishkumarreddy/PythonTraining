import json
import xmltodict

# fs = open("./source.json", "r")
# data = fs.read()
# data_dict = json.loads(data)
#
# print(data_dict)
# print(data_dict['name'])
#
#
final_output = []
with open(r"./vaccination-metadata.csv", 'r') as fs:
    n = 0
    header = []
    for row in fs.readlines():
        row = row.split(",")
        if n == 0:
            header = row
            n += 1
            continue

        new_row = {}
        for i in range(len(header) - 1):
            new_row[header[i]] = row[i]

        final_output.append(new_row)
    fs.close()
#
# final_output_json = json.dumps(final_output)
# with open(r"./outout.json",'w') as fs:
#     fs.write(final_output_json)
#     fs.close()


# fs = open("./data.xml", "r")
# data = fs.read()
# data_dict = xmltodict.parse(data)
# print(data_dict)

# final_output = json.dumps(final_output)
final_output = {"data": final_output}
mydict = {"data": {
    "emp":{
        "name": "Harish",
        "phone": 7801070710,
        "email": "harishkumarreddy.cherla@gmail.com"
    },
    "emp1":{
        "name": "Harish",
        "phone": 7801070710,
        "email": "harishkumarreddy.cherla@gmail.com"
    },
    "emp2":{
        "name": "Harish",
        "phone": 7801070710,
        "email": "harishkumarreddy.cherla@gmail.com"
    }
}}
# print(final_output)
final_output_xml = xmltodict.unparse(mydict, pretty=True)

with open(r"./outout.xml", 'w') as fs:
    fs.write(final_output_xml)
    fs.close()
