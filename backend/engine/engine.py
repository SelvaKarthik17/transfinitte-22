from t2d2 import convert_to_tree_format, get_all_people_data, get_structured_house_data, get_structured_house_data_with_people_data, group_by_house_and_address
from indgov_search import get_ind_gov_details
from utils import get_electoral_roll_pdf_url, get_pdf_from_url, create_temp_folder, get_pickle_path
from text_recognition import get_text_from_pdf
from translate import translate_locale_out
import os
import uuid
import pickle

def engine_of_program(name, age, state, voter_id, gender, relation_name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

    rand = uuid.uuid1()

    create_temp_folder()
    user_data = {
                'name': name,
                'rln_name': relation_name,
                'location': 'S22,,',
                'age': age,
                'gender': gender,
            }
    captcha_path = f'temp/{rand}-captcha.png'
    pdf_path = f'temp/{rand}.pdf'
    locale_path = f'temp/{rand}-locale-out.txt'
    english_path = f'temp/{rand}-english-out.txt'

    data = get_ind_gov_details(user_data, captcha_path)

    if data == None:
        return "Details not found",400

    pdf_url = get_electoral_roll_pdf_url(data)
    print(pdf_url)
    print(hash(pdf_url))
    pickle_path = get_pickle_path(pdf_url)

    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as f:
            people_data = pickle.load(f)
        
        house_data = get_structured_house_data_with_people_data(people_data, data['slno_inpart'])
        tree_data = convert_to_tree_format(house_data)
        
    else:

        pdf = get_pdf_from_url(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(pdf)
        get_text_from_pdf(pdf_path, locale_path)
        translate_locale_out(locale_path, english_path)

        people_data, _, _ = get_all_people_data('0', english_path)
        # pickle the people_data
        with open(pickle_path, 'wb') as f:
            pickle.dump(people_data, f)

        house_data = get_structured_house_data(data['slno_inpart'], english_path)
        tree_data = convert_to_tree_format(house_data)

    return tree_data

def get_part_family_tree(name, age, state, voter_id, gender, relation_name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

    rand = uuid.uuid1()

    create_temp_folder()
    user_data = {
                'name': name,
                'rln_name': relation_name,
                'location': 'S22,,',
                'age': age,
                'gender': gender,
            }
    captcha_path = f'temp/{rand}-captcha.png'
    pdf_path = f'temp/{rand}.pdf'
    locale_path = f'temp/{rand}-locale-out.txt'
    english_path = f'temp/{rand}-english-out.txt'

    data = get_ind_gov_details(user_data, captcha_path)

    if data == None:
        return "Details not found",400

    pdf_url = get_electoral_roll_pdf_url(data)
    pickle_path = get_pickle_path(pdf_url)

    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as f:
            people_data = pickle.load(f)
    else:

        pdf = get_pdf_from_url(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(pdf)
        get_text_from_pdf(pdf_path, locale_path)
        translate_locale_out(locale_path, english_path)

        people_data, _, _ = get_all_people_data('0', english_path)
        with open(pickle_path, 'wb') as f:
            pickle.dump(people_data, f)
    
    ha_to_people = group_by_house_and_address(people_data)

    # store the ha_to_people data in a pickle file

    starting_id = 0
    all_people = []    
    for ha, people in ha_to_people.items():
        all_people.extend(convert_to_tree_format(people, starting_id))
        starting_id += len(people)
    return all_people
