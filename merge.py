from csv_merger import CSVMerger

cm = CSVMerger()

clean_debt = "data/output/debt-gdp-percentage.csv"
clean_inflation = "data/output/inflation-gdp-percentage.csv"
clean_credit = "data/output/credit-ratings-3-2013.csv"

output = "data/output/merged-clean-data.csv"

cm.merge(clean_debt, clean_inflation, clean_credit, output)

print "Success!"