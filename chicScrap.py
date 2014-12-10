import bs4
import requests
import csv
import re

root_url = "http://www.chicagomag.com"


def make_soup(url):
    if 'http' in url:
        website = url
        response = requests.get(website)
        return bs4.BeautifulSoup(response.text)

    else:
        website = root_url+url
        response = requests.get(website)
        return bs4.BeautifulSoup(response.text)

def get_sandwich_listings(list_url):
    soup = make_soup(list_url)
    sammys = soup.findAll('div','sammyListing')
    sandwich_urls = [div.a['href'] for div in sammys]
    #print sandwich_urls
    #sandwich = [div.a.b.string for div in sammys]
    #print sandwich
    return sandwich_urls

    
def get_sandwich_data(sandwich_url):
    soup = make_soup(sandwich_url)
    sandwich = soup.find('h1','headline').string
    addy = soup.find('p','addy').em.get_text().split(',')[0].strip()
    price = addy.partition(" ")[0].strip().replace('.','')
    address = addy.partition(" ")[2].strip()
    phone = soup.find('p','addy').em.get_text().split(',')[1].strip()
    web = ""
    if soup.find('p','addy').em.a:
        web = soup.find('p','addy').em.a.get_text()
    #quote = soup.find('h2','deck').string
    #print description

    print sandwich
   # print description
#    print addy
    print price
    print address
    print phone
    print web

    return {'RankAndName':sandwich,'price':price,'address':address,'phone':phone,'website':web}



sandwich_urls = get_sandwich_listings('/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/')
"""
for url in sandwich_urls:
    print url
"""
#get_sandwich_data(sandwich_urls[12])


for url in sandwich_urls:
    print url
    get_sandwich_data(url)
    

    
