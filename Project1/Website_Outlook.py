import requests
from bs4 import BeautifulSoup
import csv
base_url = "https://www.websiteoutlook.com/"
response = requests.get(base_url)
html_soup = BeautifulSoup(response.content, 'lxml')
html_soup.title
html_soup.title.text
tables = html_soup.find_all("table")
table = tables[0]
raw_trs = table.find_all("tr")
len(raw_trs)
clean_trs = raw_trs[0:22]
raw_columns, raw_rows = clean_trs[0], clean_trs[0:]
columns = [td.text for td in raw_columns.find_all("td")]    
rows = [[td.text for td in row.find_all("td")] for row in raw_rows]
rows
myFile = open('Website_Outlook.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(['Website','Alexa Rank','Backlinks','Domain Authority'])
    writer.writerows(rows)
print("Writing complete")



