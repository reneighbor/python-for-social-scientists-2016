# one solution to end of tutorial...

import csv

class CSVMerger():


	def merge(self, debt_input, inflation_input, credit_input, output):

		countries = []

		fdebtreader = open(debt_input, 'rU')
		debtreader = csv.DictReader(fdebtreader)

		for row in debtreader:
			countries.append(row["Country Code"])

		fcreditreader = open(credit_input, 'rU')
		creditreader = csv.DictReader(fcreditreader)

		finflationreader = open(inflation_input, 'rU')
		inflationreader = csv.DictReader(finflationreader)

		fields = [
			"Country", 	
			"Moodys",
			"S&P",
			"Fitch"
			"2012-debt",
			"2012-inflation",
			"2013-debt",
			"2013-inflation"
		]

		fwriter = open(output, 'w')
		writer = csv.DictWriter(fwriter, fields, extrasaction="ignore")
		writer.writeheader()

		for country in countries:
			new_row = {"Country": country}

			for row in creditreader:
				if row['ISO code'] == country:
					print "Got a match: " + country

					new_row["S&P"] = row["S&P Rating"]
					new_row["Moodys"] = row["Moody's rating"]
					new_row["Fitch"] = row["Fitch Rating"]

			fcreditreader.seek(0)

			for row in debtreader:
				if row['Country Code'] == country:
					new_row['2013-debt'] = row["2013"]
					new_row['2012-debt'] = row["2012"]

			fdebtreader.seek(0)

			for row in inflationreader:
				if row['Country Code'] == country:
					new_row['2013-inflation'] = row["2013"]
					new_row['2012-inflation'] = row["2012"]

			finflationreader.seek(0)

			writer.writerow(new_row)



