import pandas as pd

df = pd.DataFrame(pd.read_csv('data2.csv'))
specific = None
general = []
leng = df.shape[1]-1

for i in df.itertuples():
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
