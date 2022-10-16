# remove trailing single - from each line

import re

def get_required_values(s: str):
    regex = r"^#?(?P<sno>\d+)+[\n\r\s]*([\w]+)?[\n\r\s]*Name ?:[\n\r\s]*(?P<name>[ \w$&+,:;=?@#|'<>.^*()%!-]+)[\n\r\s]*((Husband('s)? Name:[\n\r\s]*(?P<husband_name>[ \w$&+,:;=?@#|'<>.^*()%!-]+))|(Father('s)? Name ?:[\n\r\s]*(?P<father_name>[ \w$&+,:;=?@#|'<>.^*()%!-]+)))[\n\r\s]*House (Number|No)\.?:[\n\r\s]*(?P<house_number>[\da-zA-Z\-\/. ]+)[\n\r\s]*Age:[\n\r\s]*(?P<age>\d+)[\n\r\s]*(Gender)?[\n\r\s]*Gender ?:[\n\r\s]*(?P<gender>[a-zA-Z]+)[\n\r\s]*[\w\W]+address ?:[\n\r\s]*(?P<address>[\w\W]+)[\n\r\s]*"
    matches = re.finditer(regex, s, re.MULTILINE | re.IGNORECASE)
    matches = list(matches)
    for match in matches:
        return match.groupdict()
    return None


def get_block_data(block: str):
    block = block.strip()
    lines = block.split('\n')
    lines = [line.strip('-').strip() for line in lines]
    block = '\n'.join(lines)
    return get_required_values(block)


def get_all_people_data(sno, english_path: str):
    with open(english_path, encoding="utf8") as f:
        content = f.read()
    l = content.split('------------')
    l.pop()
    all_data = []
    house_number, address = None, None
    visited_snos = set()
    for block in l:
        data = get_block_data(block)
        if data == None:
            continue
        if data and data['sno'] not in visited_snos:
            if data['sno'] == sno:
                house_number, address = data['house_number'], data['address']
            all_data.append(data)
            visited_snos.add(data['sno'])
    return all_data, house_number, address

def group_by_house_and_address(data: list[dict]) -> dict:
    ha_to_people = {}
    for person in data:
        if (person['house_number'], person['address']) not in ha_to_people:
            ha_to_people[(person['house_number'], person['address'])] = []
        ha_to_people[(person['house_number'], person['address'])].append(person)
    return ha_to_people

def get_structured_house_data(sno, english_path: str) -> dict:
    people_data, house_number, address = get_all_people_data(sno, english_path)
    if house_number and address:
        ha_to_people = group_by_house_and_address(people_data)
        return ha_to_people[(house_number, address)]
    else:
        return None

def convert_to_tree_format(data: list[dict], starting_id: int = 0) -> list[dict]:
    people_to_id = {}
    people_details = {}
    for i in range(len(data)):
        people_to_id[data[i]['name']] = i + starting_id
        people_details[i + starting_id] = {}
        people_details[i + starting_id]['id'] = i + starting_id
        people_details[i + starting_id]['name'] = data[i]['name']
        people_details[i + starting_id]['pids'] = []
        people_details[i + starting_id]['gender'] = data[i]['gender'].lower()
    for i in range(len(data)):
        if data[i]['father_name'] and data[i]['father_name'] in people_to_id:
            people_details[i + starting_id]['fid'] = people_to_id[data[i]['father_name']]
        if data[i]['husband_name'] and data[i]['husband_name'] in people_to_id:
            people_details[i + starting_id]['pids'].append(people_to_id[data[i]['husband_name']])
            people_details[people_to_id[data[i]['husband_name']]]['pids'].append(i + starting_id)
    # add mid if pid of fid is present
    for i in range(len(data)):
        if 'fid' in people_details[i + starting_id]:
            fid = people_details[i + starting_id]['fid']
            if 'pids' in people_details[fid] and len(people_details[fid]['pids']) == 1:
                people_details[i + starting_id]['mid'] = people_details[fid]['pids'][0]
    return list(people_details.values())


if __name__ == '__main__':
    sno = input('Enter S.No: ')
    data = get_structured_house_data(sno)
    if data:
        print(convert_to_tree_format(data))
    else:
        print('No data found')
