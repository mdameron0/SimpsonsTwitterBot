#used to scrape links to episodes, was not used in final product.
#Beutiful soup is a XML/HTML parsing library.
#link to beutiful soup site/docs: http://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup
import urllib2

#opens the file we will be putting the links in.
textFile = open("LinkList.txt", "w")

#page we will scrape the links from
wikiToScrape = "http://simpsons.wikia.com/wiki/List_of_episodes"

#create a soup object to search with the HTML of the above link
soup = BeautifulSoup(urllib2.urlopen(wikiToScrape))

#finds all the <a> tags with Href properties (Links)
tag = soup.find_all('a', href=True)




for i in tag:
	textFile.write(i['href'] + "\n")

textFile.close()