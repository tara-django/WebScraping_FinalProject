import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://en.wikipedia.org/wiki/List_of_largest_technology_companies_by_revenue"
response = requests.get(base_url)
html_soup = BeautifulSoup(response.content, 'lxml')

tables = html_soup.find_all("table")

table = tables[1]
raw_trs = table.find_all("tr")
len(raw_trs)
clean_trs = raw_trs[0:22]
raw_columns, raw_rows = clean_trs[0], clean_trs[1:]
rows = [[td.text for td in row.find_all("td")] for row in raw_rows]
rows
myFile = open('TOP_IT_Company.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(['Rank','','Company','Fiscal Year Ending','Revenue $b USD','Employees','HeadQuaters'])
    writer.writerows(rows)
    
print("Writing complete")