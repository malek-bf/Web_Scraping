
Web Scraping with Beautifulsoup
=

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/README.md?color=3776AB&logo=python&logoColor=3CB371)

Overview
=
Web Scraping is the ideal solution for extracting data from the web. 
It makes the job easier and more ready for work.

Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 
It commonly saves programmers hours or days of work.

Check the Beautifulsoup homepage at https://www.crummy.com/software/BeautifulSoup/bs4/doc/ for more information, including a list of features.

Requirements
=
* Python 2.7+
* Works on Linux, Windows, macOS, BSD

Step1
----
Installing the required libraries:

Easiest way to install external libraries in python is to use pip. pip is a package management system used to install and manage software packages written in Python.

All you need to do is:

    pip install bs4
    
    pip install requests
    
    pip install lxml
    
=> It’s essential to install lxml

Step2
----
Accessing the HTML content from webpage:

    import requests 
    source = requests.get('https://www.hotnewhiphop.com/top100/').text
    
First of all import the requests library.

Then, specify the URL of the webpage you want to scrape

Step3
---
Parsing the HTML content:

    import requests 
    from bs4 import BeautifulSoup

    source = requests.get('https://www.hotnewhiphop.com/top100/').text
    soup = BeautifulSoup(source, 'lxml')
    
 Step4
 ---
 Searching and navigating through the parse tree:
 
 Now, we are going to extract some useful data from the HTML content. The soup object contains all the data in the nested structure which could be programmatically extracted.
 
 In our example, we are scraping the top100 songs from  https://www.hotnewhiphop.com/
 
 So, we would like to create a program to save those Top100Songs (and all relevant information about them).
 
 It is noticed that all the information that we need are inside a "div" or "li" container . So, we find that "div" or "li" element  using find() or find_all() method and mention the   id of that container
 
 for expl:
 
         scrape_element in soup.find_all('li',class_='chartItem')
         
  we use find_all() method which is similar to find method in terms of arguments but it returns a list of all matching elements
  
  Step5
  ---
  Finally, we would like to save all our data in some CSV file:
  
    import csv
    
    csv_project=open('my_scraping_project.csv','w',newline='')
    csv_writer=csv.writer(csv_project)
    
  We create the new CSV file when we “open” it using “csv.writer”
  
  The “w” tells the computer to “write” to the file. And to keep everything organized, let’s write some column headers.
  
  As each line is processed, the rank,song_name,artist and link information is written to our CSV file.
  
    csv_writer.writerow([rank, song_name,artist,final_link])

 
 

                                              
    


  

    

    
    

  









