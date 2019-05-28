"""1. pip install requests
API request code """
import requests, json

url = "https://api-chiatai.23perspective.com/api/cms_admin/login"
payload = {"username":"admin@admin.com","password":"12345678"}
headers = {'content-type': 'application/json'}

r = requests.post(url,data=json.dumps(payload),headers=headers) #post request  to login

print("Response Code = ",r.status_code) ###response code ex: 200,404,502

# response = r.text ###response msg send back as text
# print(response)

if(r.json()["response_code"] == 200): ###if 200 print token --> request.json()["JSON part U want"]
	print(r.json()["response_msg"])### pick data from response, In this case we pick response_msg
	print(r.json()["result"]["token"])### pick data from response, In this case we pick Token in Result
	print("    ")
	#print(r.encoding)
	token = r.json()["result"]["token"]
else: 
	print(r.json())
	###print(r.json()["response_msg"])### pick data from response, In this case we pick response_msg

geturl = "https://api-chiatai.23perspective.com/api/cms_user/get_list"
get_header = {"Authorization":token} #header with token from above API
params = {"perpage":10,"page":1} #fill parameter
getlist = requests.get(geturl,params=params,headers=get_header)
print(getlist.json())