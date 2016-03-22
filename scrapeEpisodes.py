#Beutiful soup is a XML/HTML parsing library.
#link to beutiful soup site/docs: http://www.crummy.com/software/BeautifulSoup/
#there is some editing you have to do once the file is compiled, I think it was 4 lines I had to remove. They are just things that are presented at the top of the page.
from bs4 import BeautifulSoup
import urllib2

#this is the page with the information of episodes I want.
wikiToScrape = "https://simple.wikipedia.org/wiki/List_of_The_Simpsons_episodes"

#create a soup object with the HTML of wikiToScrape
soup = BeautifulSoup(urllib2.urlopen(wikiToScrape))

#looks for all <tr> tags and compiles them
tag = soup.find_all('tr')

#open the TextFile we will be adding the lines to.
textFile = open("EpisodeList.txt", "w")

#itterate through the <tr> tags and getting all the <td> tags within.
#count is used to fix some lines that are blank in the tables provided.
for g in tag:
	count = 0
	textFile.write("\n") 
	for k in g.find_all('td'):
		if count == 3:
			try:
				textFile.write(str(k.a.text) + " ")
			except:
				pass
		elif count == 4 or count == 2:
			pass
		else:
			textFile.write(str(k.string) + " ")
		count+=1

#housekeeping 
textFile.close()