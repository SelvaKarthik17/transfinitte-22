from indgov_search import get_ind_gov_details
from utils import get_electoral_roll_pdf_url, get_pdf_from_url
import dotenv
from text_recognition import get_text_from_pdf

dotenv.load_dotenv()

# data = {
#     "pc_name": "KALLAKURICHI",
#     "st_code": "S22",
#     "ps_lat_long_1_coordinate": 0,
#     "gender": "M",
#     "rln_name_v2": "",
#     "rln_name_v1": "செல்வநாயகம் ",
#     "rln_name_v3": "",
#     "name_v1": "பிரதீப் ",
#     "epic_no": "NSY2434637",
#     "ac_name": "Kallakurichi",
#     "name_v2": "",
#     "name_v3": "",
#     "ps_lat_long": "0.0,0.0",
#     "pc_no": "14",
#     "last_update": "Thu Jan 06 12:33:24 IST 2022",
#     "id": "S220800020010050",
#     "dist_no": "33",
#     "ps_no": "20",
#     "ps_name": "Roman Catholic Middle School, South Side West Wing North Face, Kallakurichi-606202",
#     "ps_name_v1": "ரோமன் கத்தோலிக்க நடுநிலைப்பள்ளி, தெற்கு பக்கம் மேற்கு பகுதி வடக்கு முகம், கள்ளக்குறிச்சி-606202",
#     "st_name": "Tamil Nadu",
#     "dist_name": "Kallakurichi",
#     "rln_type": "F",
#     "pc_name_v1": "கள்ளக்குறிச்சி",
#     "part_name_v1": "ரோமன் கத்தோலிக்க நடுநிலைப்பள்ளி, தெற்கு பக்கம் மேற்கு பகுதி வடக்கு முகம், கள்ளக்குறிச்சி-606202",
#     "ac_name_v1": "கள்ளக்குறிச்சி",
#     "part_no": "20",
#     "dist_name_v1": "கள்ளக்குறிச்சி",
#     "ps_lat_long_0_coordinate": 0,
#     "_version_": 1721202905987416065,
#     "name": "Pradeep ",
#     "section_no": "1",
#     "ac_no": "80",
#     "slno_inpart": "50",
#     "rln_name": "Selvanayagam ",
#     "age": 19,
#     "part_name": "Roman Catholic Middle School, South Side West Wing North Face, Kallakurichi-606202",
#     "hashedInfo": "412bc07613a4a15cb1c16a57965d6e258ca54a1ea66244168086c0e2ad0339d080e37f872c4c3ec6a2e164bc9a4250a30f5a81cacdce383c0eea1fdfd1a92fe7",
#     "enc_epic_no": "rBLhcWpv18W6UX9sA9ZOlA=="
# }

data = get_ind_gov_details()

print(data)

PDF_PATH = 'temp/test.pdf'

pdf_url = get_electoral_roll_pdf_url(data)
pdf = get_pdf_from_url(pdf_url)
print(pdf_url)
with open(PDF_PATH, 'wb') as f:
    f.write(pdf)
get_text_from_pdf(PDF_PATH)

