#lucas hom web scraper

import requests
import csv
from BeautifulSoup import BeautifulSoup

#webpage url
url = 'http://online.wsj.com/mdc/public/page/2_3062-nasdaqshort-highlites.html#shortD'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs = {'class': 'mdcTable'})

#put table into list of rows and cells inside rows

list_rows = [] #make list for rows
for row in table.findAll('tr')[1:]:
	list_cells = [] #array for row
	for cell in row.findAll('td'):
   		text = cell.text.replace('&nbsp;', '') #replace nonbreaking space
   		list_cells.append(text)
   	list_rows.append(list_cells)

outfile = open("./stocks.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["number","company","symbol", "date1","date2","change","percentChange", "percentFloat","daysToCover","avgDailyVolume" ])
writer.writerows(list_rows)

#lucas hom
