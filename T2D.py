import re

def get_structured_house_data(data: dict):
    with open('temp/english-out.txt', encoding="utf8") as f:
        lines = f.readlines()
    # print(lines)
    sno = str(data['slno_inpart']) #need to search by serial, not part number

    d = {}
    houseNumber = 0
    hn = 0
    for i in range(len(lines)):
        if lines[i].startswith(sno):
            houseNumber = lines[i+3]
            break
    number = lines[0][:-1]
    temp = {}
    for i in range(len(lines)):
        if lines[i].startswith("Available"):
            if str(sno) == number:
                hn = houseNumber
            if houseNumber not in d:
                d[houseNumber] = [temp]
            else:
                d[houseNumber].append(temp)
            if i+1 < len(lines):
                number = lines[i+2][:-1]
            temp = {}
        else:
            if lines[i].startswith("Name") and (lines[i+1].startswith("Father") or lines[i+1].startswith("Husband")):
                temp["name"] = lines[i][5:-2]
            elif lines[i].startswith("Name"):
                temp["name"] = lines[i][5:-2] + lines[i+1]
            elif (lines[i].startswith("father") or lines[i].startswith("Father")) and lines[i+1].startswith("House"):
                temp["father"] = lines[i][12:-2]
            elif (lines[i].startswith("father") or lines[i].startswith("Father")) and len(lines[i].split(" ")) < 4:
                temp["father"] = lines[i+1][:-2]
            elif (lines[i].startswith("father") or lines[i].startswith("Father")):
                temp["father"] = lines[i][12:-2] + lines[i+1]
            elif (lines[i].startswith("husband") or lines[i].startswith("Husband")) and lines[i+1].startswith("House"):
                temp["husband"] = lines[i][13:-2]
            elif (lines[i].startswith("husband") or lines[i].startswith("Husband")) and len(lines[i].split(" ")) < 4:
                temp["husband"] = lines[i+1][:-2]
            elif (lines[i].startswith("husband") or lines[i].startswith("Husband")):
                temp["husband"] = lines[i][13:-2] + lines[i+1]
            elif lines[i].startswith("Age"):
                temp["age"] = lines[i].split(" ")[1]
                temp["gender"] = lines[i].split(" ")[3][:-1]
            elif lines[i].startswith("House"):
                houseNumber = re.sub('[^A-Za-z0-9]+', '', lines[i].split(" ")[2][:-1]).upper()
    return d[str(hn)]

# converting to below format
# [
#     { id: 1, pids: [2], name: 'Amber McKenzie', gender: 'female', img: 'https://cdn.balkan.app/shared/2.jpg'  },
#     { id: 2, pids: [1], name: 'Ava Field', gender: 'male', img: 'https://cdn.balkan.app/shared/m30/5.jpg' },
#     { id: 3, mid: 1, fid: 2, name: 'Peter Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/2.jpg' },
#     { id: 4, mid: 1, fid: 2, name: 'Savin Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/1.jpg'  },
#     { id: 5, mid: 1, fid: 2, name: 'Emma Stevens', gender: 'female', img: 'https://cdn.balkan.app/shared/w10/3.jpg' }
# ]

def convert_to_tree_format(data: list[dict]) -> list[dict]:
    people_to_id = {}
    people_details = {}
    for i in range(len(data)):
        people_to_id[data[i]['name']] = i
        people_details[i] = {}
        people_details[i]['id'] = i
        people_details[i]['name'] = data[i]['name']
        people_details[i]['pids'] = []
        people_details[i]['gender'] = data[i]['gender'].lower()
    for i in range(len(data)):
        if 'father' in data[i] and data[i]['father'] in people_to_id:
            people_details[i]['fid'] = people_to_id[data[i]['father']]
        if 'husband' in data[i] and data[i]['husband'] in people_to_id:
            people_details[i]['pids'].append(people_to_id[data[i]['husband']])
            people_details[people_to_id[data[i]['husband']]]['pids'].append(i)        

    return list(people_details.values())
