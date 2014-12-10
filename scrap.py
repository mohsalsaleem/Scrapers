import bs4
from urllib2 import urlopen
import requests

root_url = "http://www.chicagoreader.com"

def make_soup(url):
    website = root_url+url
    response = requests.get(website)
    return bs4.BeautifulSoup(response.text)


def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find('dl','boccat')
    category_links = [dd.a['href'] for dd in boccat.findAll('dd')]
    return category_links

def get_category_winner(category_link):
    soup = make_soup(category_link)
    website = root_url+category_link
    category = soup.find("h1","headline").string
    #print category
    winner = [h2.string for h2 in soup.findAll('h2','boc1')]
    #print winner
    runners_up = [h2.string for h2 in soup.findAll('h2','boc2')]
    
    result = {"Category":category,
            "Link":website,
            "Winner":winner,
            "Runners_up":runners_up}
    return result


category_links = get_category_links('/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228')
#print category_links
#print get_category_winner(category_links[0])
#print len(category_links)

for link in category_links:
    winner_list = get_category_winner(link)
    print "\n\n\n"
    print "=================="+winner_list['Category']+"============="+'\n'
    print "Link to the page: "+winner_list['Link']
    print "Winner(s):"
    for winner in winner_list['Winner']:
        print winner
    print "Runners Up:"
    for runner in winner_list['Runners_up']:
        print runner
    print "\n\n"    

    
