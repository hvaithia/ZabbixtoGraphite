#!/usr/bin/env python
#!/usr/bin/python -u

import json
import urllib2
import sys
import globals

########Get login auth token from login class##########
#auth=python_login()
#url = 'http://10.13.4.84//zabbix/api_jsonrpc.php'
############################################################

########## Function test get alerts################
def get_alert(objectid):
	obj =  {"jsonrpc": "2.0","method": "event.get","params":{"output": "extend","objectids": objectid},"auth": globals.auth,"id": 1}
	data = json.dumps(obj)
	request = urllib2.Request(globals.url, data, {'Content-Type': 'application/json'})
	response = urllib2.urlopen(request)
	res = json.load(response)
	if 'error' in res:
		print 'An error occurred! %s' %res["error"]
		sys.exit(-1)
	print "result string is %s" %(res["result"])
	return res["result"]

#get_alert(13913)
