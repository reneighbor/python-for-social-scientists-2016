TALK INTRODUCTIONS
------------------

1. Introduce self. Name, programming experience / what you're interested in learing this for.

1. Introduce self to partner. You will ask each other Qs / copy each 
other's stuff if you fall behind. 

1. However feel free to interrupt and ask the class **at any time**.


SETUP
-----

1. First, open up a text editor. If you don't have one,
download Sublime for your operating system:
http://www.sublimetext.com/2

1. Go to github repo for sample code: bit.ly/python-social, (aka
https://github.com/reneighbor/python-for-social-scientists-2016).
Copy the URL from your browser.

1. Using the command line, go into the directory where you keep your coding projects.

1. Run the following command:
`git clone https://github.com/reneighbor/python-for-social-scientists-2016`

1. You should now have `python-for-social-scientists-2016` as a directory. Open up
that entire directory in your text editor.


PART ONE
--------

1. We are researchers looking at the various ways a country can be econmically healthy. World Bank provides lots of data.

1. Let's check out the `data` folder in Github together. One is particularly small, `data/originals/sample.csv`.

1. Note: During this lesson it's OK to just copy/paste the code samples. Implementation details do matter, but we'll be able to cover more ground if we focus more on overall trends.

1. (From in `starter.py`). Read in this file using csv DictReader, print each row:
		

```python
	import csv

	f = open('data/originals/sample.csv', 'rU')

	reader = csv.DictReader(f)

	for row in reader:
		print row

	print "Success!"
```

1. (Copy/paste). Make use of dictionary structure to access values by key:

```python
	import csv

	f = open('data/originals/sample.csv', 'rU')

	reader = csv.DictReader(f)

	for row in reader:
		print row["Country Code"]
		print row["2013"]

	print "Success!"
```


1. Do the same for large data set. First, delete lines 1-4 in `data/originals/debt-gdp-percentage.csv`. Then, run the code below:

```python
	import csv

	f = open('data/originals/debt-gdp-percentage.csv', 'rU')

	reader = csv.DictReader(f)

	for row in reader:
		print row["Country Code"]
		print row["2013"]

	print "Success!"
```


1. We want to remove all columns but country code and years. Actually, we want to preserve original data file- make a NEW file of only relevant columns. `DictReader` was a class to read CSV files. `DictWriter` is what we'll use.

1. `DictReader` class took file handler. `DictWriter` class takes handler for file destination, **and** `fields` (column headers), as well as optional params:

```python
	import csv

	freader = open('data/originals/debt-gdp-percentage.csv', 'rU')
	fwriter = open('data/output/debt-gdp-percentage.csv', 'w')

	fields = ["Country Code"]

	for year in range(1960, 2015):
		fields.append(str(year))

	reader = csv.DictReader(freader)
	writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")

	writer.writeheader()

	for row in reader:
		writer.writerow(row)

	print "Success!"
```

1. Open the new file up in Google Drive, validate it looks as expected.

1. We want to stop doing the manual having to skip first 4 lines lines. `freader` is just a pointer to file/data, so use it to skip lines:

```python
	import csv 

	def skip_lines(fp, numlines):	
			for i in range(numlines):
			    fp.next()


	freader = open("data/originals/debt-gdp-percentage.csv", 'rU')
	skip_lines(freader, 4)

	fwriter = open("data/output/debt-gdp-percentage.csv", 'w')

	fields = ["Country Code"]

	for year in range(1960, 2015):
		fields.append(str(year))

	reader = csv.DictReader(freader)
	writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")

	writer.writeheader()

	for row in reader:
		writer.writerow(row)

	print "Success!"
```


1. Do the same for a different indicator. Q: What would change compared to above? A: Just the filename.

1. Make it a function:

```python
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
```
1. And in your `starter.py`:

```python
	inflation_input = "data/originals/inflation-gdp-percentage.csv"
	inflation_output = "data/output/inflation-gdp-percentage.csv"

	debt_input = "data/originals/debt-gdp-percentage.csv"
	debt_output = "data/output/debt-gdp-percentage.csv"

	standardize_tables(inflation_input, inflation_output)
	standardize_tables(debt_input, debt_output)

	print "Success!"
```


1. Great! What did we do? 
	* 	Input a csv file to python 
	*	Re-wrote file to only include relevant columns 
	* 	Went from deleting top 4 lines manually to writing a function
	* 	Made re-writing a reusable function for other files from this source

1. Now, let's say we're a researcher and we want to share this code with colleague down the hall. 

1. Or, let's say the World Bank comes out with updated data every quarter, we want this to be a recurring job.

1. Cut and paste this code? I don't think so.

1. Make it a module! Then your `starter.py` script becomes very simple, only imports and uses our module.

1. In order to make our code a module, we need to:
	* Add `Class()` declaration
	* Add `self` argument to method calls
	* Add `self` to method call for `skip_lines`

1. Make a new file, `wb_standardizer.py`, and paste in this code:

```python
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
```


1. Change your `starter.py`:

```python
	from wb_standardizer import WBStandardizer


	inflation_input = "data/originals/inflation-gdp-percentage.csv"
	inflation_output = "data/output/inflation-gdp-percentage.csv"

	debt_input = "data/originals/debt-gdp-percentage.csv"
	debt_output = "data/output/debt-gdp-percentage.csv"


	wb = WBStandardizer()

	wb.standardize_tables(inflation_input, inflation_output)
	wb.standardize_tables(debt_input, debt_output)

	print "Success!"
```

1. Considerations: Note that starter.py has all the specific context about file location.

1. By contrast, `wb_standardizer` should be able to act independently 
of file location context. It just needs to know about World Bank formatting.


BREAK
-----

PART TWO
--------

1. What did we do before break?
	* Looked at data in human-friendly interface (Github, Excel).
	* Read in file and looked at output using Python.
	* Removed columns using Python (actually wrote new file).
	* Removed first 4 lines using Python (also new file).
	* Made our code a function.
	* Made our code a module.

1. We want to also examine Moody's data on credit ratings.
What challenge do we face if we merge this table with the others?

1. We want to translate 3-digit country codes as 2-digit.
Google "python country code converstion", find `pycountry`,
let's read it together.

1. Copy/paste from the sample code into your `starter.py` (comment out the other stuff):
	
```python
	import pycountry
	germany = pycountry.countries.get(alpha2='DE')
	print germany.alpha3
```

1. Validate that pycountry does what you want. (Copy/paste):
	
```python
	import pycountry

	germany = pycountry.countries.get(alpha2='DE')

	alpha3 = germany.alpha3
	alpha2 = germany.alpha2
```

1. OK. Now that we've validated that this works, what kind of function do we want to write?

1. We want to write a function where argument is one type (alpha3), output is other type (alpha2).

```python	
	def translate_country_code(self, alpha3_code):
		country = pycountry.countries.get(alpha3=alpha3_code)
		return country.alpha2
```


1. Handle case where there is no match:
	
```python
	def translate_country_code(self, alpha3_code):
		try:
			country = pycountry.countries.get(alpha3=alpha3_code)
			return country.alpha2
		except:
			return "**"
```			


1. Ok we've found a source to translate country codes and made a

1. How will we use this in our function? Look at `wb_standardizer`.
`for row in reader` -- each row is a dictionary.

1. We will replace country code before writing it.

```python
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
```


1. Credit ratings. What do you need to do to standardize it?
	* Skip lines - no
	* Delete non-useful columns? yes
	* Translate country code? no

1. Should be able to write standardizer class for ratings, as a review. Do it with your partner.