from t2d2 import convert_to_tree_format, get_all_people_data, get_structured_house_data, group_by_house_and_address
from indgov_search import get_ind_gov_details
from utils import get_electoral_roll_pdf_url, get_pdf_from_url, create_temp_folder
from text_recognition import get_text_from_pdf
from translate import translate_locale_out
import os

def engine_of_program(name, age, state, voter_id, gender, relation_name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

    create_temp_folder()
    user_data = {
                'name': name,
                'rln_name': relation_name,
                'location': 'S22,,',
                'age': age,
                'gender': gender,
            }
    data = get_ind_gov_details(user_data)
    PDF_PATH = 'temp/test.pdf'

    pdf_url = get_electoral_roll_pdf_url(data)
    pdf = get_pdf_from_url(pdf_url)
    with open(PDF_PATH, 'wb') as f:
        f.write(pdf)
    get_text_from_pdf(PDF_PATH)
    translate_locale_out()
    house_data = get_structured_house_data(data['slno_inpart'])
    tree_data = convert_to_tree_format(house_data)  

    return tree_data

def get_part_family_tree(name, age, state, voter_id, gender, relation_name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

    create_temp_folder()
    user_data = {
                'name': name,
                'rln_name': relation_name,
                'location': 'S22,,',
                'age': age,
                'gender': gender,
            }
    data = get_ind_gov_details(user_data)
    PDF_PATH = 'temp/test.pdf'

    pdf_url = get_electoral_roll_pdf_url(data)
    pdf = get_pdf_from_url(pdf_url)
    with open(PDF_PATH, 'wb') as f:
        f.write(pdf)
    get_text_from_pdf(PDF_PATH)
    translate_locale_out()

    people_data, _, _ = get_all_people_data('0')
    ha_to_people = group_by_house_and_address(people_data)
    starting_id = 0
    all_people = []    
    for ha, people in ha_to_people.items():
        all_people.extend(convert_to_tree_format(people, starting_id))
        starting_id += len(people)
    return all_people
