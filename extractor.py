import re
import requests
from bs4 import BeautifulSoup,CData
import urllib
import sys


#site = 'http://pixabay.com'
basesite = 'https://www.bing.com/images/search?q=sanchi+temple+TORANA&qs=n&form=QBIR&sp=-1&pq=sanchi+temple+torana&sc=0-20&sk=&cvid=8A61FBCC1DAB4350BAC4B08D82877E77'
site= basesite + '&format=PBXML'
filename_initial= "TORANA"
filename_urls= filename_initial + '.txt'
TXT= filename_initial + '_all.txt'

response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
count=0
urls=[]
for line in soup:
    line= str(line)
    splitted_line= line.split()
    partnum=0
    for part in splitted_line:
        partnum+=1
        if "MediaUrl" in part:
            new_url=splitted_line[partnum+1][1:-2]
            urls.append(new_url)
            with open(filename_urls,"a") as f:
                f.write(new_url+ "\n") 
                
'''                
urls1=[]
for line in soup:
    line= str(line)
    splitted_line= line.split()
    partnum=0
    for part in splitted_line:
        if "http" in part:
            new_url=part[1:-2]
            urls1.append(new_url)
            with open(TXT,"a") as f:
                f.write(new_url+ "\n") 


'''





















#            with open("myurls.txt", 'wb') as f:
#                response = requests.get(splitted_line[partnum+1])
#                f.write(response.content)
 
      
                          

#print(site)
'''

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all(attrs={'class': 'MediaUrl'})

urls = [img['src'] for img in img_tags]
print urls



for url in urls:
    print url
    if 'http' not in url:
            continue
    filename = re.search(r'/([\w_-]+[.](JPG|jpg|gif|png))$', url)
    if filename == None:
        resource = urllib.urlopen(url)
        output = open("file01.jpg","wb")
        output.write(resource.read())
        print 'here'
        continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            continue
            print "yes"
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format('https://', url)
        print url
        response = requests.get(url)
        f.write(response.content)
    print ('done')
    

'''
