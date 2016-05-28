import csv
import pycountry

class WBStandardizer():

	def standardize_tables(self, inpath, outpath):
		
		freader = open(inpath, 'rU')
		self.skip_lines(freader, 4)
		reader = csv.DictReader(freader)

		fields = ["Country Code"]

		for year in range(1960, 2015):
			fields.append(str(year))

		fwriter = open(outpath, 'w')
		writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")
		writer.writeheader()

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