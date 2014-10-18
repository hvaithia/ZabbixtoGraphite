#!/usr/bin/env python
#!/usr/bin/python -u

import sys
import time
from gethosts import get_hosts
from getstackid import parse_stackID
from graphitetcp import send_content

def keys_to_graphite(key_list):
	stackids = parse_stackID("/home/local/MYFAMILYSOUTH/dc_hvaithianathan/zabbix_python/core_stack_list.csv")
	dicthostnames = get_hosts()
	netcat_string=""
	for idx, val in enumerate(key_list):
		for j in range(len(val["result"])):
			try:
				hostname = dicthostnames[val["result"][j]['hostid']]
			except Exception, e:
				#print e
				continue
			#zabbix_key = val["result"][j]['key_'].split('.')[-1]
			zabbix_key = val["result"][j]['key_'].replace(".", "_").replace("/","_")
			zabbix_value = val["result"][j]['lastvalue']
			try:
				stack_id = stackids[hostname].upper()
				if stack_id == "":
					stack_id = "UNKNOWN"
			except:
				stack_id = "UNKNOWN"
			#print "%s.%s.%s %s %d" %(stack_id,hostname,zabbix_key,zabbix_value,int(time.time()))
			netcat_string=netcat_string+stack_id+"."+hostname+"."+zabbix_key+" "+zabbix_value+ " "+ str(int(time.time()))+"\n"
	print netcat_string
	send_content(netcat_string)


