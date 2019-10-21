import csv

with open('data.csv') as df:
	readcsv = csv.reader(df,delimiter=',')
	data = []
	for row in readcsv:
		if row[len(row)-1] == "yes":
			data.append(row)
print("+ examples:")
for i in data:
	print(i)
TotalPos = len(data)
hypo = None

for row in data:
	for j in range(len(row)-1):
		if hypo == None:
			hypo = row
		else:
			if hypo[j] != row[j]:
				hypo[j] = "?"
hypo.pop()
print("Hypothesis:",hypo)
test_case = input().split()
flag = True
for i in range(len(test_case)):
	if hypo[i] != '?':
		if hypo[i]!=test_case[i]:
			flag = False
if flag==True:
	print("Yes")
else:
	print("No")
			
