from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import random,pickle,time

class IP:
	def __init__(self):
		self.ua = UserAgent()
		self.proxies = []
		self.file=open('ip.txt','rb')
		self.proxies=pickle.load(self.file)
		self.file.close()

	def random_proxy(self):
	  return random.randint(0,len(self.proxies)-1)
	
	def ip(self):
		for n in range(1, 50):
			start_time = time.time()
			proxy_index = self.random_proxy()
			proxy = self.proxies[proxy_index]
			req = Request('http://icanhazip.com')
			req.set_proxy(proxy,'http')
			try:
				my_ip = urlopen(req).read().decode('utf8')
				f=time.time() - start_time
				break
			except Exception as e:
				print("E")
		return self.ua,proxy
		
	
	