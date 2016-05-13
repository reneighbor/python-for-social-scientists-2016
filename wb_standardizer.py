import csv
import pycountry

class WBStandardizer():

	def standardize_tables(self, inpath, outpath):
		
		# Create file reader and skip first 4 lines
		freader = open(inpath, 'rU')
		self.skip_lines(freader, 4)
		reader = csv.DictReader(freader)

		# Specify the fields we ultimately want
		fields = ["Country Code"]

		for year in range(1960, 2015):
			fields.append(str(year))

		# Create start of output CSV file
		fwriter = open(outpath, 'w')
		writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")
		writer.writeheader()

		# Write rest of output file
		for row in reader:
			row["Country Code"] = self.translate_country_code(row["Country Code"])
			writer.writerow(row)


	def skip_lines(self, fp, numlines):	
		for i in range(numlines):
		    fp.next()

	def translate_country_code(self, alpha3_code):
		try:
			country = pycountry.countries.get(alpha3=alpha3_code)
			return country.alpha2
		except:
			return "**"
			