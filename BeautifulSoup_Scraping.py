#Loading the necessary libraries

import requests
from bs4 import BeautifulSoup
import csv

# Open the output file for writing before the loop
csv_project=open('scraping_project.csv','w',newline='')
csv_writer=csv.writer(csv_project)
# Write column headers as the first line
csv_writer.writerow(['rank','song_name','artist','link'])

#Load the web page content
source = requests.get('https://www.hotnewhiphop.com/top100/').text

#Convert to a beautiful soup object
soup = BeautifulSoup(source, 'lxml')



for scrape_element in soup.find_all('li',class_='chartItem'):
 try:

    for start in scrape_element.find_all('div', class_="chartItem-body-artist"):
     rank = scrape_element.span.em.text
     print(rank)

     song_name = scrape_element.find('div', class_="chartItem-body-artist").a.text
     print(song_name)

     artist = scrape_element.find('div', class_='chartItem-artist-info').strong.text
     print(artist)

     for link in start.find_all('a', href=True):

      char = link['href'][:1]

      if "//" not in link['href']:
       if char != '/':
        print(link['href'])

      if (char == '/'):
       base_link = 'https://www.hotnewhiphop.com/'
       final_link = base_link + link['href'][1:]
       print(final_link)
    print()

    csv_writer.writerow([rank, song_name,artist,final_link])

 except Exception as e:
  pass #This tells the computer to move on to the next item after it encounters an error



csv_project.close()


