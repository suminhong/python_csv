import csv

path = 'C:/sample.csv'

try:
	f = open(path, encoding='euc-kr')
	csv_f = csv.reader(f)

	for line in csv_f:
		print(line[0], '\t', line[1], '\t', line[2], '\t', line[3], '\t', line[4])

except Exception as e:
    print(e)