import re
import urllib

def getPublicIp():
	data = str(urllib.urlopen('http://checkip.dyndns.com/').read())
	return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

def currentLocation(ip=getPublicIp()):
	response = urllib.urlopen('http://api.hostip.info/get_html.php?ip='+ip+'&position=true').read()
	return response