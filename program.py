from wb_standardizer import WBStandardizer
from ratings_standardizer import RatingsStandardizer

wt = WBStandardizer()

wb_inpath = "data/worldbank/originals/inflation-gdp-percentage.csv"
wb_outpath = "data/worldbank/output/inflation-gdp-percentage.csv"
wt.standardize_tables(wb_inpath, wb_outpath)


rt = RatingsStandardizer()

rt_inpath = "data/ratings/originals/credit-ratings-3-2013.csv"
rt_outpath = "data/ratings/output/credit-ratings-3-2013.csv"
rt.standardize_tables(rt_inpath, rt_outpath)