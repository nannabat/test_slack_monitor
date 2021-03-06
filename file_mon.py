#!/usr/bin/python
import pyinotify,subprocess,json,slack_bot_alert,socket,create_incident

ABS_PATH_AGENT_CONF_FILE='/root/spy_script_py/agentconfig.json'
CONF_MODIFIED=False
#intial_value_list = get_values_list()

def get_values_list():
	config_file = open(ABS_PATH_AGENT_CONF_FILE,'r')
	configurations = json.load(config_file)
	return_dict_values = {}
	for scriptname,time_value in configurations.items():
		return_dict_values[scriptname] = time_value
	return return_dict_values

def get_changed_values_dict():
	current_values_dict = get_values_list()
	return_changed_values_dict = {}
        #tmp_intial_value_list = intial_value_list
	for script_name in current_values_dict.keys():
		if intial_value_list[script_name] != current_values_dict[script_name]:
			return_changed_values_dict[script_name] = current_values_dict[script_name]
        global intial_value_list
	intial_value_list = current_values_dict
	return return_changed_values_dict

def onChange(ev):
    #cmd = ['/bin/echo',ABS_PATH_AGENT_CONF_FILE, ev.pathname, 'changed']
    #subprocess.Popen(cmd).communicate()
    #CONF_MODIFIED = True
    print 'changed values are:'
    tmp_dict = get_changed_values_dict()
    changed_values_json = json.dumps(tmp_dict, ensure_ascii=False)
    #print json.dumps(changed_values_json, indent=4)
    HOSTNAME = socket.gethostname()
    ALERT = 'File monitoring alert: value/values in file: %s on host %s' %(ABS_PATH_AGENT_CONF_FILE,HOSTNAME)
    DETAILS = 'changed values are: \t' + str(changed_values_json)
    srv_now_response = create_incident.create_tkt(DETAILS,ALERT)
    TKT_NUMBER = srv_now_response['result']['number']
    #NON_ATTACH_TEXT = 'File monitoring alert,ticket ' + TKT_NUMBER + 'is created'
    slack_bot_alert.send_alert_to_slack(ALERT,DETAILS,TKT_NUMBER)
    return changed_values_json

    # for script_name,time_value in tmp_dict.items():
    # 	tmp_script_name = script_name + '.py'
    	

		

global intial_value_list
intial_value_list = get_values_list()
    		
if __name__ == '__main__':
	wm = pyinotify.WatchManager()
	wm.add_watch(ABS_PATH_AGENT_CONF_FILE, pyinotify.IN_CLOSE_WRITE, onChange)
	notifier = pyinotify.Notifier(wm)
	#print "the value of CONF_MODIFIED: " + str(CONF_MODIFIED)
	#global intial_value_list
        #intial_value_list = get_values_list() 
        print intial_value_list
	notifier.loop()
