from flask import Flask, request, Response
import json
import requests

app = Flask(__name__)


user = 'ops_bot'
pwd = 'root'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
url = 'https://dev27484.service-now.com/api/88257/slackintegraion'

@app.route('/ticketstatus')
def fetch_status():
	number_var = str(request.args['text'])
	data_var = {
	"action": "status",
	"ticket_info":{
	"number":number_var
	}
	}

	response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data_var, ensure_ascii=False))
	if response.status_code != 200: 
	    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
	    exit()
	# Decode the JSON response into a dictionary and use the data
	#print response.get_data()
	#print 'type of response is:' + str(type(response))
	json_response_from_service_now = json.dumps(response.json(),indent = 4)
	#print 'type of json response is:' + str(type(json.dumps(response.json(),indent = 4)))
	json_response_from_service_now_dict = json.loads(json_response_from_service_now)
	status_code = json_response_from_service_now_dict['result']['status']
	assigned_to_var = json_response_from_service_now_dict['result']['assigned_to']
	state_var = json_response_from_service_now_dict['result']['state']
	su_message_var = 'this is assigned to:' + assigned_to_var + 'status is: ' + state_var
	su_message_assign = {"text":su_message_var}
	fa_message_assign = {"text":"Unable to assign to you"}

	print 'status is:' + status_code

	print json_response_from_service_now_dict
	if status_code == 'success':
		return Response(json.dumps(su_message_assign, ensure_ascii=False), status=200, mimetype="application/json")
	else:
		return Response(json.dumps(fa_message_assign, ensure_ascii=False), status=200, mimetype="application/json")

@app.route('/assignme')
def assign_to_me():
	number_var = str(request.args['text'])
	assigned_to_var = str(request.args['user_name'])
	su_message_assign = {"text":"Assigned  to you successfully"}
	fa_message_assign = {"text":"Unable to assign to you"}

	data_var = {
	"action": "update",
	"ticket_info":{
	"assigned_to":assigned_to_var,
	"number":number_var
	}
	}
	response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data_var, ensure_ascii=False))
	if response.status_code != 200: 
	    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
	    exit()
	# Decode the JSON response into a dictionary and use the data
	#print response.get_data()
	#print 'type of response is:' + str(type(response))
	json_response_from_service_now = json.dumps(response.json(),indent = 4)
	#print 'type of json response is:' + str(type(json.dumps(response.json(),indent = 4)))
	json_response_from_service_now_dict = json.loads(json_response_from_service_now)
	status_code = json_response_from_service_now_dict['result']['status']
	print 'status is:' + status_code

	print json_response_from_service_now_dict
	if status_code == 'updated':
		return Response(json.dumps(su_message_assign, ensure_ascii=False), status=200, mimetype="application/json")
	else:
		return Response(json.dumps(fa_message_assign, ensure_ascii=False), status=200, mimetype="application/json")





@app.route('/addworknotes')
def worknotes():
	# usage: /addworknotes INC02345:the comments are very useful
	su_message = {"text":"Worknotes updated successfully"}
	fa_message = {"text":"Worknotes failed to update"}
	arguments = request.args['text']
	print arguments
	#print request.user_name
	args_list = arguments.split(':')
	work_notes_var = str(request.args['user_name']) + ':' + str(args_list[1])
	data_var = {
	"action": "update",
	"ticket_info":{
	"work_notes":work_notes_var,
	"number":str(args_list[0]),
	}
	}
	response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data_var, ensure_ascii=False))

	# Check for HTTP codes other than 200
	if response.status_code != 200: 
	    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
	    exit()
	# Decode the JSON response into a dictionary and use the data
	#print response.get_data()
	#print 'type of response is:' + str(type(response))
	json_response_from_service_now = json.dumps(response.json(),indent = 4)
	#print 'type of json response is:' + str(type(json.dumps(response.json(),indent = 4)))
	json_response_from_service_now_dict = json.loads(json_response_from_service_now)
	status_code = json_response_from_service_now_dict['result']['status']
	print 'status is:' + status_code

	print json_response_from_service_now_dict
	if status_code == 'updated':
		return Response(json.dumps(su_message, ensure_ascii=False), status=200, mimetype="application/json")
	else:
		return Response(json.dumps(fa_message, ensure_ascii=False), status=200, mimetype="application/json")

if __name__ == '__main__':
	app.run(port=5005,debug=True)
