import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.flightstats.com/v2/flight-tracker/departures/KTM"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'lxml')

csv_file = open('flight_arrival.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['FLIGHT','FLIGHT NUMBER','ARRIVAL TIME','DESTINATION'])

for table in soup.find_all('a', class_="table__A-s1x7nv9w-2 flrJsE"):
    
    flight = table.find('div', class_='table__Cell-s1x7nv9w-13 iZEpOT').text
    print(flight)
    
    flight_no = table.find('div', class_='table__Cell-s1x7nv9w-13 Ltznn').text
    print(flight_no)
    
    departure = table.find('div', class_="table__Cell-s1x7nv9w-13 nqUsN").text
    print(departure)

    arrival = table.find('div', class_="table__OrangeCell-s1x7nv9w-14 jJXjoY table__Cell-s1x7nv9w-13 nqUsN").text
    print(arrival)
    
    destination = table.find('div', class_="table__Cell-s1x7nv9w-13 hUDiRd").text
    print(destination)
    
    print()
    
    csv_writer.writerow([flight ,flight_no, departure, arrival, destination])
    
csv_file.close()
