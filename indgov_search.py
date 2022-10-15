import requests
from captcha_solver import solve_captcha
import requests

def get_ind_gov_details():
	tries = 10

	while tries > 0:
		cookies = {
			'Electoral': '456c656374726f6c7365617263682d73657276657234',
			'Electoral': '456c656374726f6c7365617263682d73657276657234',
			'cookiesession1': '678B2867FFB16F1E02B1283C8A931300',
			'runOnce': 'true',
			'electoralSearchId': 'xetigxgmpvlzqmcefwlcw1hk',
			'__RequestVerificationToken': 'FCwqEXXu4x5T37b7yfzBS56V7gSVKz8twSo-2QzOm36kr9bPALSRGxakDfRKPcEgqhTef3acSLBbDqNwaDgxEwQkuAwgVMMKvZHlbem8pDk1',
		}

		headers = {
			'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8',
			'Connection': 'keep-alive',
			# Requests sorts cookies= alphabetically
			# 'Cookie': 'Electoral=456c656374726f6c7365617263682d73657276657234; Electoral=456c656374726f6c7365617263682d73657276657234; cookiesession1=678B2867FFB16F1E02B1283C8A931300; runOnce=true; electoralSearchId=xetigxgmpvlzqmcefwlcw1hk; __RequestVerificationToken=FCwqEXXu4x5T37b7yfzBS56V7gSVKz8twSo-2QzOm36kr9bPALSRGxakDfRKPcEgqhTef3acSLBbDqNwaDgxEwQkuAwgVMMKvZHlbem8pDk1',
			'Referer': 'https://electoralsearch.in/',
			'Sec-Fetch-Dest': 'image',
			'Sec-Fetch-Mode': 'no-cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
			'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Linux"',
		}

		response = requests.get(
			'https://electoralsearch.in/Home/GetCaptcha?image=true&id=Sat%20Oct%2015%202022%2000:29:23%20GMT+0530%20(India%20Standard%20Time)', cookies=cookies, headers=headers)


		file = open("captcha.png", "wb")
		file.write(response.content)
		file.close()

		captcha = solve_captcha('captcha.png').strip()

		#########################


		cookies = {
			'Electoral': '456c656374726f6c7365617263682d73657276657234',
			'Electoral': '456c656374726f6c7365617263682d73657276657234',
			'cookiesession1': '678B2867FFB16F1E02B1283C8A931300',
			'runOnce': 'true',
			'electoralSearchId': 'xetigxgmpvlzqmcefwlcw1hk',
			'__RequestVerificationToken': 'FCwqEXXu4x5T37b7yfzBS56V7gSVKz8twSo-2QzOm36kr9bPALSRGxakDfRKPcEgqhTef3acSLBbDqNwaDgxEwQkuAwgVMMKvZHlbem8pDk1',
		}

		headers = {
			'Accept': 'application/json, text/plain, */*',
			'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8',
			'Connection': 'keep-alive',
			'Content-Type': 'application/json;charset=UTF-8',
			# Requests sorts cookies= alphabetically
			# 'Cookie': 'Electoral=456c656374726f6c7365617263682d73657276657234; Electoral=456c656374726f6c7365617263682d73657276657234; cookiesession1=678B2867FFB16F1E02B1283C8A931300; runOnce=true; electoralSearchId=xetigxgmpvlzqmcefwlcw1hk; __RequestVerificationToken=FCwqEXXu4x5T37b7yfzBS56V7gSVKz8twSo-2QzOm36kr9bPALSRGxakDfRKPcEgqhTef3acSLBbDqNwaDgxEwQkuAwgVMMKvZHlbem8pDk1',
			'Origin': 'https://electoralsearch.in',
			'Referer': 'https://electoralsearch.in/',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
			'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Linux"',
		}

		json_data = {
			'txtCaptcha': captcha,
			'search_type': 'details',
			'reureureired': 'ca3ac2c8-4676-48eb-9129-4cdce3adf6ea',
			'name': 'pradeep',
			'rln_name': 'selvanayagam',
			'page_no': 1,
			'location': 'S22,,',
			'results_per_page': 10,
			'location_range': '20',
			'age': 20,
			'dob': None,
			'gender': 'M',
		}

		print(json_data)
		print(cookies)
		print(headers)

		response = requests.post('https://electoralsearch.in/Home/searchVoter',
								cookies=cookies, headers=headers, json=json_data)

		print(response.text)

		if response.text == 'Wrong Captcha':
			tries -= 1
			print('Wrong Captcha')
			print('failed attempts: ', 10 - tries)
		else:
			print('Success')
			break

	print(response.json())

	docs = response.json()["response"]["docs"]
	if len(docs) == 0:
		print("No results found")
		exit(0)

	return docs[0]
