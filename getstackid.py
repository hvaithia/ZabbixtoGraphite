#!/usr/bin/env python
#!/usr/bin/python -u

import sys
import os
import shutil 

def parse_stackID(csvfile):
	host_stack={}
	f=open(csvfile,'rU')
	for line in f.readlines():
		y = line.strip().split(",")
		host_stack[y[0].upper()]=y[2]
	#print host_stack
	return host_stack

#parse_stackID("core_stack_list.csv")
