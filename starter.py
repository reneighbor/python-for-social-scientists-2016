import csv

f = open('data/originals/sample.csv', 'rU')

reader = csv.DictReader(f)

for row in reader:
	print row

print "Success!"