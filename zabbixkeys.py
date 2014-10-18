#!/usr/bin/env python
#!/usr/bin/python -u

import json
import urllib2
import sys
import time
import globals
from keystographite import keys_to_graphite

########Get login auth token from login class##########

auth = globals.auth
url = globals.url

#########Function send item key values to get jsonresponse################

def define_keys():
	####Simply add any key from zabbix items and its charted in graphite. How cool is that!###
	key_list=["vfs.fs.size[C:,free]","vfs.fs.size[D:,free]","vfs.fs.size[D:,pfree]","vfs.fs.size[C:,pfree]","vfs.fs.size[D:,total]","vfs.fs.size[C:,total]","vfs.fs.size[C:,used]","vfs.fs.size[D:,used]","net.if.out[Microsoft Hyper-V Network Adapter]","net.if.out[Microsoft Hyper-V Network Adapter-WFP LightWeight Filter-0000]","net.if.out[Microsoft Hyper-V Network Adapter-QoS Packet Scheduler-0000]","vfs.fs.size[/usr,free]","vfs.fs.size[/var,free]","vfs.fs.size[/home,free]","vfs.fs.size[/boot,free]","vfs.fs.size[/,free]","vfs.fs.size[/usr,pfree]","vfs.fs.size[/home,pfree]","vfs.fs.size[/var,pfree]","vfs.fs.size[/boot,pfree]","vfs.fs.size[/,pfree]","net.if.in[eth0]","net.if.out[eth0]","system.swap.size[,free]","system.cpu.util[,user]","system.cpu.util[,system]","system.cpu.util[,idle]","system.cpu.load[percpu,avg1]","system.cpu.load[percpu,avg5]","vm.memory.size[total]","system.swap.size[,total]"]
	#key_list=["system.cpu.util[,user]","system.cpu.util[,idle]"]
	json_list=[]
	#print key_list
	for index, value in enumerate(key_list):
		a=get_jsonresponse(value)
		json_list.append(a)
	#print json_list,"\n\n"
	keys_to_graphite(json_list)

########## Function test get specific items from each hosts################

def get_jsonresponse(key):
	#obj = {"jsonrpc": "2.0","method": "item.get","params": {"output": "extend","filter":{"hostid":"10119","key_":"vfs.fs.size[C:,free]"}},"auth": auth,"id": 3}
	obj = {"jsonrpc": "2.0","method": "item.get","params": {"output": "extend","filter":{"key_":key}},"auth": auth,"id": 3}
	data = json.dumps(obj)
	request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	response = urllib2.urlopen(request)
	res = json.load(response)
	if 'error' in res:
		print 'An error occurred! %s' %res["error"]
		sys.exit(-1)
	return res

#define_keys()
