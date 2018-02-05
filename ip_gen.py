
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random,pickle,sys
from get_ip import IP
from bs4 import BeautifulSoup

#sys.setrecursionlimit(2000)

def random_proxy():
  return random.randint(0,len(proxies)-1)

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]
#i=IP()
#b,ip=i.ip()

#scrapping ip's
proxies_req = Request('https://www.sslproxies.org/')

#adding header to request
proxies_req.add_header('User-Agent', ua.random)
#proxies_req.set_proxy(ip,'http')

proxies_doc = urlopen(proxies_req).read().decode('utf8')
soup = BeautifulSoup(proxies_doc, 'html.parser')
proxies_table = soup.find(id='proxylisttable')

for row in proxies_table.tbody.find_all('tr'):
	#proxies.append({'ip':   row.find_all('td')[0].string,'port': row.find_all('td')[1].string})
	proxies.append(row.find_all('td')[0].string+':'+row.find_all('td')[1].string)

ips=[]

'''
try:
	file=open('ip.txt','rb')
	ips=pickle.load(file)
	file.close()
except:
	file.close()

#file.close()
print(len(ips))
'''

#print(proxies)
#proxies=ips
#now ips are generated
#checking valid ips
proxies=ips+proxies


for n in range(1, 100):
	proxy_index = random_proxy()
	proxy = proxies[proxy_index]
	req = Request('http://icanhazip.com')
	#setting proxy to request
	req.set_proxy(proxy,'http')
	try:
		my_ip = urlopen(req).read().decode('utf8')
		print( str(n) +" IP:" + my_ip)
		#break
	except Exception as e: # If error, delete this proxy and find another one
		del proxies[proxy_index]
		print('Proxy ' + proxy+ ' deleted.')

file=open('ip.txt','wb+')
pickle.dump(proxies,file)
file.close()