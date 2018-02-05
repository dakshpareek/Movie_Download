print("Content-type:text/html\r\n\r\n")
print('''<html>
<head></head>
<body>
''')
import pickle
f=open("movies_data.txt","rb")
data=pickle.load(f)

#print(data[0][1])
for j,i in enumerate(data):
	#print(i)
    print("<h2><a href=movie.py/{}>{}</a></h2>".format(j,i[0]))

print('''
</body>
</html>
''')