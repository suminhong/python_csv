import csv

path = 'C:/sample.csv'

try:
	f = open(path, 'a', encoding='euc-kr', newline='')
	csv_f = csv.writer(f)

	csv_f.writerow([400, '인턴', '이', '2019-04-01', 24])

except Exception as e:
    print(e)