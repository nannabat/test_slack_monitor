#Need to install requests package for python
#easy_install requests
import requests,json

def create_tkt(DETAILS,ALERT):
	# Set the request parameters
	#url = 'https://dev27484.service-now.com/api/now/table/incident'
	url = 'https://dev27484.service-now.com/api/88257/slackintegraion'

	# Eg. User name="admin", Password="admin" for this code sample.
	user = 'ops_bot'
	pwd = 'root'

	# Set proper headers
	headers = {"Content-Type":"application/json","Accept":"application/json"}

	# Do the HTTP request
	data_var = {
	"action": "insert",
	"ticket_info":{
	"short_description":DETAILS,
	"description":ALERT
	}
	}
	response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data_var, ensure_ascii=False))

	# Check for HTTP codes other than 200
	if response.status_code != 200: 
	    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
	    exit()
	# Decode the JSON response into a dictionary and use the data
	data = response.json()
	print(data)
	return data
