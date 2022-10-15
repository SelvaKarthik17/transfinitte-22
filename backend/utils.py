import requests

import os

def create_temp_folder():
    if not os.path.exists("temp"):
        os.makedirs("temp")
    
def get_electoral_roll_pdf_url(data):
    base_url = "https://www.elections.tn.gov.in/SSR2022_MR_05012022"
    part1 = "/dt" + data["dist_no"]
    part2 = "/ac" + data["ac_no"].zfill(3)
    part3 = "/ac" + data["ac_no"].zfill(3) + data["part_no"].zfill(3) + ".pdf"
    final_url = base_url + part1 + part2 + part3
    return final_url

def get_pdf_from_url(url):
    response = requests.get(url)
    return response.content
