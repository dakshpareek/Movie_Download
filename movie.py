print("Content-type:text/html\r\n\r\n")
print('''<html>
<head></head>
<body>
''')
import pickle,os,cgi
from pickle import load


f=open("movies_data.txt","rb")
data=pickle.load(f)

sid=os.environ['PATH_TRANSLATED']
id=sid.split('\\')
id=int(id[-1])


img=data[id][1][0]
final=data[id][1][1]

for i in img:
	print("<img src='{}'>".format(i))

print("<a href='{}'>Download</a>".format(final))
print('''
</body>
</html>
''')