import csv

specific = None
general = []
with open('data2.csv') as df:
	readcsv = csv.reader(df,delimiter=',')
	data = []
	for row in readcsv:
		leng = len(row)-1
		row.insert(0,1)
		data.append(row)
data.pop(0)

for i in data:
	if i[-1]=='p':
		if specific==None:
			specific = list(i[1:-1])
		else:
			k = 0
			for j in i[1:-1]:
				if specific[k]!=j and specific[k]!='?':
					specific[k] = '?'
				k+=1
	else:
		k = 0
		for j in i[1:-1]:
			if specific[k]!=j and specific[k]!='?':
				g = ['?']*leng
				g[k] = specific[k]
				if g not in general:
					general.append(g)
			k+=1
	for li in general:
		for ele in range(len(li)):
			if specific[ele]=='?' and li[ele]!='?':
				general.remove(li)
				break
print(specific)
print('*'*30)
print(general)