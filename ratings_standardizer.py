import csv
import re

class RatingsStandardizer():

	def standardize_tables(self, inpath, outpath):

		freader = open(inpath, 'rU')
		reader = csv.DictReader(freader)

		fields = [
			"ISO code",
			"S&P Rating",
			"Moody's rating",
			"Fitch Rating"
		]
		
		fwriter = open(outpath, 'w')
		writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")		
		writer.writeheader()

		for row in reader:
			writer.writerow(row)

 