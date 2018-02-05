#!C:\Python36\python.exe 
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import cgi
from pickle import dump,load
import json,random
import time
from get_ip import IP

class Movie:
	def __init__(self):
		try:
			self.f1=open('movies_data.txt','rb')
			self.prev=load(self.f1)
			self.f1.close()
		except:
			self.prev=[]
		self.i=IP()
	
	def get_ip(self):
		#geeting new ip and header	
		return self.i.ip()
		
	def make_request(self,url,browser,ip):
		#creating request
		proxies_req = Request(url)
		proxies_req.add_header('User-Agent', browser)
		proxies_req.set_proxy(ip,'http')
		print(ip)
		return proxies_req
	def scrape_data(self,n):
		#generating request and getting data
		browser,ip=self.get_ip()
		browser=browser.random
		url = "http://extramovies.cc/page/"+str(n)
		pro_req=self.make_request(url,browser,ip)

		html = urlopen(pro_req).read().decode('utf8')
		soup=BeautifulSoup(html,"lxml")
		movies = soup.findAll("div", {"class": "thumbnail"})
		all_data=[]
		prev_title=[]
		for i in self.prev:
			prev_title.append(i[0])
			
		for every_movie in movies:
			a_tag=every_movie.findAll("a")
			title=a_tag[0].attrs["title"]
			link=a_tag[0].attrs["href"]
			if title not in prev_title:
				sample=[title,self.get_download_links(link,browser,ip)]		
				all_data.append(sample)
				print("Scrapped")
				#time.sleep(3)
		
		new_title=[]

		for i in all_data:
			new_title.append(i[0])
		for i in range(len(new_title)):
			if new_title[i] not in prev_title:
				self.prev.append(all_data[i])
		f1=open('movies_data.txt','wb+')
		dump(self.prev,f1,protocol=2)
		f1.close()
		print("Done")
	
	def get_download_links(self,url,browser,ip):
		movie_link=Request(url)
		movie_link.add_header('User-Agent', browser)
		movie_link.set_proxy(ip,'http')
		html = urlopen(movie_link).read().decode('utf8')
		soup=BeautifulSoup(html,"lxml")	
		img=soup.findAll("img",{"class": "alignnone"})
		d_link=soup.findAll("a",{"class": "buttn blue"})
		f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
				
		movie_link =Request(f_link)
		movie_link.add_header('User-Agent', browser)
		movie_link.set_proxy(ip,'http')
				
		html = urlopen(movie_link).read().decode('utf8')
		soup2=BeautifulSoup(html,"lxml")
		last_link=soup2.findAll("a")
		final=last_link[len(last_link)-2].attrs["href"]
		images=[]
		for j in range(1,len(img)):
			k=img[j].attrs["src"]
			images.append(k)
		#result=[images,final]		
		#completed.append(result)
		return images,final
#getting new movie links 
#mv=Movie()
pages=range(16,141)
for i in pages:
	mv=Movie()
	print("Page"+str(i))
	mv.scrape_data(i)
	#mv.get_download_links()

#mv.scrape_data('4')

#getting download links of movies
#mv.get_download_links()