#!/usr/bin/env python
#!/usr/bin/python -u
import json
import urllib2
import sys

#from login import python_login

###This class is to define the global variables###

url = 'http://10.13.1.64//zabbix/api_jsonrpc.php'
graphitehost='host.domain.com'
graphiteport='2013' ###Enter your carbon port
zabbixUserUI="Admin"	###Enter zabbix UI admin name
zabbixPassword="zabbix"		###Enter zabbix UI password

"""
This function returns the auth token for Zabbix which can be used for other JSON calls
"""
def python_login():
        obj = {"jsonrpc": "2.0","method": "user.login","params": {"user": zabbixUserUI,"password": zabbixPassword},"id": 0}

        data = json.dumps(obj)
        request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(request)
        res = json.load(response)
	#print res
        #auth = "34740fca6b70102f4dc27bf0a72b00a1"
        hash_pass=[]

        if 'error' in res:
                # An error occurred; raise an exception
                print 'An error occurred! %s' %res["error"]
                sys.exit(-1)

        try:
                hash_pass=res["result"]
                return hash_pass
        except:
                hash_pass=res["error"]["data"]
                print hash_pass
                sys.exit()
        print "Auth token is %s" %(hash_pass)

auth=python_login()
#print auth
