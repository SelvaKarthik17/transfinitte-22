
# Transfinitte-22

### Developers

- [Tharun A](https://github.com/tharun571)
- [Pradeep S](https://github.com/pradeep-707)
- [Arnav Menon](https://github.com/arnavmenon)
- [Hari Rahul](https://github.com/haribaz)
- [Ashwath Niranjh](https://github.com/ashwathniranjh)
- [Selva Karthik](https://github.com/SelvaKarthik17)
---
### Steps to setup API locally

1. Clone the Repo 
```
git clone https://github.com/SelvaKarthik17/transfinitte-22.git
```
2. Create python virtual environmnent
```
python -m venv venv
```
3. Navigate to the backend folder
```
cd backend
```
4. Install packages from requirements.txt
```
pip install -r requirements.txt
```
4. Download two key files provided in drive link attached in google form and paste it in the backend directory
5. Start the server
```
python app.py
```
The server will be up on port 5000.

- Website Link - [Family Ties](https://family-ties.selvakarthik.me/)
- API Link - [https://transfinitte-api.selvakarthik.me/](https://transfinitte-api.selvakarthik.me/)

- *Note to the reader: The API will be down whenever our GCP account runs out of credit since costs will be incurred for the usage of GCP services. Please ping the API economically. If it doesn't work replicate the server locally and use your own GCP APIs(DocumentAI, Cloud Vision, Google Translation)*
- *New calls to the API take about 7-8 mins. If you're looking to get faster responses try out one of the requests in the postman link. Those constituencies are cached in the system*

- Postman Link - [Postman Workspace](https://web.postman.co/haribaz/workspace/my-workspace/request/17759945-b5e48199-1410-4a93-a0a1-c8ec6526c9d7)


### API endpoints:
- GET **/** - general GET request to server - returns hello world
- POST **/** - POST request to get family tree details of a particular person
- POST **/getAllPartFamilies** - POST request to get all family trees in constituency of person queried. 

### Response Format
A JSON data is returned from backend which represents the family tree of that specific person(for / route), or the family tree for all families in the constituency of query (for /getAllPartFamilies route).
The JSON format is as follow:
```
[
	{
		"fid":"string",
		"mid":"string",
		"gender":"string",
		"id":"string",
		"pids":["string"],
		"name":"string",
	},
	.
	.
	.
]
```

here,
- fid: id of the father
- mid: id of the mother
- pids: id of partners
- gender: gender of person
- name: name of person
- id: unique tree id of person
