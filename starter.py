# Starter file for data manipulation workshop. 
# Start off by viewing "data/worldbank/originals/" files
# in Excel / Google Spreadhseets and manually deleting non-tabluar data

import csv

f = open('data/originals/sample.csv', 'rU')

reader = csv.DictReader(f)

for row in reader:
	print row 