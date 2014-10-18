#!/usr/bin/env python
#!/usr/bin/python -u

import json
import urllib2
import sys
#from login import python_login
import globals

########Get login auth token from login class##########
auth=globals.auth
url = globals.url
obj = {"jsonrpc": "2.0","method": "host.get","params": {"output": "extend"},"auth": auth,"id": 2}      #gives all hosts info - Tested
host_list=[]
############################################################

########## Function get hosts################
def get_hosts():
	data = json.dumps(obj)
	request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	response = urllib2.urlopen(request)
	res = json.load(response)
	if 'error' in res:
		print 'An error occurred! %s' %res["error"]
		sys.exit(-1)
	hostid_name={}	########## This is the dict of hostid and hostname###########
	for i in range(len(res["result"])):
		#print "hostid is %s | hostname is %s" %(res["result"][i]['hostid'],res["result"][i]['name'])
		hostid_name[res["result"][i]['hostid']]=res["result"][i]['name'].upper()
		#host_list.append(res["result"][i]['hostid'])
	#print host_list
	#print hostid_name
	return hostid_name	#####dict is returned######
#get_hosts()
