# 1) Introduce self. Name, What you currently do, Programming experience / any projects done recently

# 2) Download file, open it up in Google Drive, look at it. 
# 3) Import file into software using csv DictReader, print each row

'''
import csv

f = open('data/debt-gdp-percentage.csv', 'rU')

reader = csv.DictReader(f)

for row in reader:
	print row

	print row["Country Code"]
	print row["2014"]
'''

# 4) Want to remove all columns but country code and years. Actually, we want to preserver original data file- make a NEW file of only relevant columns,
# DictReader class takes file handler. DictWriter class takes handler for file destination, fields (column headers), optional params

'''
import csv 


freader = open('data/worldbank/originals/debt-gdp-percentage.csv', 'rU')
fwriter = open('data/worldbank/output/debt-gdp-percentage.csv', 'w')

fields = ["Country Code"]

for year in range(1960, 2015):
	fields.append(str(year))

reader = csv.DictReader(freader)
writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")

writer.writeheader()

for row in reader:
	writer.writerow(row)
'''

# 5) Open up in Google Drive, validate it looks as expected

# 5.5) Want to stop doing the manual skip lines. freader is just a pointer to file/data

'''
import csv 

def skip_lines(fp, numlines):	
		for i in range(numlines):
		    fp.next()


freader = open("data/worldbank/originals/debt-gdp-percentage.csv", 'rU')
skip_lines(freader, 4)

fwriter = open("data/worldbank/output/debt-gdp-percentage.csv", 'w')

fields = ["Country Code"]

for year in range(1960, 2015):
	fields.append(str(year))

reader = csv.DictReader(freader)
writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")

writer.writeheader()

for row in reader:
	writer.writerow(row)
'''


# 6) Do the same for a different indicator. What would change compared to above? Just the filename
# Try it and make sure it works.

# 7) Make it a function.

'''
import csv 

def skip_lines(fp, numlines):	
		for i in range(numlines):
		    fp.next()


def standardize_tables(inpath, outpath):
	freader = open(inpath, 'rU')
	skip_lines(freader, 4)

	fwriter = open(outpath, 'w')

	fields = ["Country Code"]

	for year in range(1960, 2015):
		fields.append(str(year))

	reader = csv.DictReader(freader)
	writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")

	writer.writeheader()

	for row in reader:
		writer.writerow(row)




inflation_input = "data/worldbank/originals/inflation-gdp-percentage.csv"
inflation_output = "data/worldbank/output/inflation-gdp-percentage.csv"

debt_input = "data/worldbank/originals/debt-gdp-percentage.csv"
debt_output = "data/worldbank/output/debt-gdp-percentage.csv"

standardize_tables(inflation_input, inflation_output)
standardize_tables(debt_input, debt_output)

'''


# 8) Great! What did we do? 
# Input a csv file to python 
# Re-wrote file to only include relevant columns 
# Went from deleting top 4 lines manually to writing a function
# Made re-writing a reusable function for other files from this source

# 9) Let's say we're a researcher and we want to share this code with colleague down the hall. 
# Or let's say WB comes out with updated data every quarter, we want this to be a recurring job.
# Cut and paste this code? I don't think so.

# Make it a module! Then your starter.py becomes very simple, only imports and uses our module

# Need to:

# * Add class() declaation
# * add self to method calls
# * add self to method call for skip_lines

# wb_standardizer.py:
'''
import csv 

class WBStandardizer():

	def skip_lines(self, fp, numlines):	
			for i in range(numlines):
			    fp.next()


	def standardize_tables(self, inpath, outpath):
		freader = open(inpath, 'rU')
		self.skip_lines(freader, 4)

		fwriter = open(outpath, 'w')

		fields = ["Country Code"]

		for year in range(1960, 2015):
			fields.append(str(year))

		reader = csv.DictReader(freader)
		writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")

		writer.writeheader()

		for row in reader:
			writer.writerow(row)

'''

#starter.py:
'''
from wb_standardizer import WBStandardizer


inflation_input = "data/worldbank/originals/inflation-gdp-percentage.csv"
inflation_output = "data/worldbank/output/inflation-gdp-percentage.csv"

debt_input = "data/worldbank/originals/debt-gdp-percentage.csv"
debt_output = "data/worldbank/output/debt-gdp-percentage.csv"


wb = WBStandardizer()

wb.standardize_tables(inflation_input, inflation_output)
wb.standardize_tables(debt_input, debt_output)
'''

# Considerations: Starter.py has all the specific context about file location, how you *use* the input/output. 
# wb_standardizer should 
# be able to act independently for any context as long as it fits the World Bank data format

# Show using / importing the module

# BREAK

# Want to also examine Moody's data
# Go over challenge of countries with merging
# We want to translate 3-digit country codes as 2-digit
# Google "python country code converstion"
# write function that takes input/output 3digit/2digit, use functionin existing module


'''
import pycountry

germany = pycountry.countries.get(alpha2='DE')

print germany.alpha3

'''

# OK. Now that we've validated that this works, what kind of function do we want to write?
# Function where argument is one type (alpha 3), output is other type

'''
def translate_country_code(self, alpha3_code):
	country = pycountry.countries.get(alpha3=alpha3_code)
	return country.alpha2
'''

# Handle case where there is no match

'''
	def translate_country_code(self, alpha3_code):
		try:
			country = pycountry.countries.get(alpha3=alpha3_code)
			return country.alpha2
		except:
			return "**"
			
'''


# Ok we've found a source to translate country codes
# How will we use this in our function. Look at WB standardizer
# for row in reader -- each one is a dictionary
# replace country code before writing it.

'''
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
'''


# Credit ratings. What do you need to do to standardize it?
# Skip lines - no
# Delete non-used columns? yes
# Translate country code? No

# Should be able to write country standardizer, as a review. Do it together.