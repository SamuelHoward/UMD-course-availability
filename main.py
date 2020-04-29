# Testing web scraping using requests and BeautifulSoup in Python

# Import requests and BeautifulSoup
import sys
import requests
from bs4 import BeautifulSoup

# Use requests module to access webpage and save it
result = requests.get("https://app.testudo.umd.edu/soc/search?courseId=" +
                      sys.argv[1]
                      + "&sectionId=&termId=202008&openSectionsOnly=true&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on")

# Print status code for site, 200 means the site is accessible
#print(result.status_code)

# Print HTTP header of site
#print(result.headers)

# store site content
src = result.content
#print(src)

# Use BeautifulSoup to parse and process a webpage
soup = BeautifulSoup(src, 'lxml')

# Use find_all to find all links on the page
pcs = soup.find_all("div", {"class": "course"})

# loop through links to filter them
for pc in pcs:

    print('{:16}'.format(pc.get('id')) +
          pc.find("span", {"class": "course-title"}).text.strip())

    secs = pc.find_all("div", {"class": "section-info-container"})
    
    for sec in secs:

        print('{:16}'.format(sec.find("span", {"class": "section-id"}).text.strip()) +
              '{:32}'.format(sec.find("span", {"class": "section-instructor"}).text.strip()) +
              '{:3}'.format(sec.find("span", {"class": "open-seats-count"}).text.strip()) +
              " / " +
              '{:3}'.format(sec.find("span", {"class": "total-seats-count"}).text.strip())
        )

    print
        
        
