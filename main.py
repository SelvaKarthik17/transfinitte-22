from t2d2 import convert_to_tree_format, get_structured_house_data
from indgov_search import get_ind_gov_details
from utils import get_electoral_roll_pdf_url, get_pdf_from_url, create_temp_folder
from text_recognition import get_text_from_pdf
from translate import translate_locale_out
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

create_temp_folder()
user_data = {
			'name': 'ashwath niranjh',
			'rln_name': 'anandaraman',
			'location': 'S22,,',
			'age': 21,
			'gender': 'M',
		}
data = get_ind_gov_details(user_data)
# print(data)
# PDF_PATH = 'temp/test.pdf'

# pdf_url = get_electoral_roll_pdf_url(data)
# pdf = get_pdf_from_url(pdf_url)
# print(pdf_url)
# with open(PDF_PATH, 'wb') as f:
#     f.write(pdf)
# get_text_from_pdf(PDF_PATH)
# translate_locale_out()
house_data = get_structured_house_data(data['slno_inpart'])
tree_data = convert_to_tree_format(house_data)  
print(tree_data)
