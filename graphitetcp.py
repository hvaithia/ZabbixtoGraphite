#!/usr/bin/env python
#!/usr/bin/python -u

import sys
import subprocess
import globals

hostname=globals.graphitehost
port=globals.graphiteport

#### netcat sends the content to graphite via tcp strem ###

def send_content(content):
	ncstring="echo "+ "'"+content+ "'"+ "| nc "+hostname+" "+port
	#print ncstring
	p=subprocess.Popen(ncstring, stdout=subprocess.PIPE,shell=True)
	output, err = p.communicate()
