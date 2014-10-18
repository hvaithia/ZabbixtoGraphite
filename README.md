###Zabbix2Graphite###

#This project is created to send data from Zabbix to graphite.
#Graphite is a powerful dashboarding tool, where the input info can be collected from different ways like StatsD, collectD etc
#This project is to send data from Zabbix (a powerful monitoring tool) to Graphite
#The information is sent to Graphite using netcat bash utility. So pre-req involves installing nc program. "yum install nc"
#Feeding the data to carbon can be done in many ways, "http://graphite.readthedocs.org/en/1.0/feeding-carbon.html". I use the plaintext protocol to do so using TCP connection with netcat
#I have tested this with Carbon daemon in background for receiving metrics and whisper database. I use Elasticsearch to save the dashboards with Grafana as frontend UI. The version of graphite used is 0.9.x
#we have a stackID in our infrastructure, so I would have used it in this code for stackID integration. You can just omit getstackid and modify the keystographite.py 
#	file to omit the stackID in the netcat_string
#zabbixtographite.py should be run as a cron for the data to be sent as stream. I run it every 4 minutes. Below is my cron
#*/4 * * * * /usr/bin/python /path/to/graphite/file/zabbixtographite.py 

#Please suggest any improvements for the project. I used subprocess with netcat because the tcp sockets in python posed a problem to send data to graphite 
#and receive response

