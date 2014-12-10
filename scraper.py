import requests
import bs4
import re
from multiprocessing import Pool
import webbrowser
import io
#website = raw_input()

root_url = 'http://pyvideo.org'
index_url = '/category/50/pycon-us-2014'

def get_video_page_urls():
    website = root_url+index_url
    response = requests.get(website)
    #print response.text
    soup = bs4.BeautifulSoup(response.text)
    #links = soup.select('div.video-summary-data a[href^=/video]')
    links = [a.attrs.get('href') for a in soup.select('div.video-summary-data a[href^=/video]')]
    return links

#print get_video_page_urls()
def get_video_data(video_page_url):
    video_data = {}
    response = requests.get(root_url+video_page_url)
    soup = bs4.BeautifulSoup(response.text)
    video_data['title'] = soup.select('div#videobox h3')[0].get_text()
    video_data['speakers'] = [a.get_text() for a in soup.select('div#sidebar a[href^=/speaker]')]
    video_data['youtube_url'] = soup.select('div#sidebar a[href^=http://www.youtube.com]')[0].get_text()
    response = requests.get(video_data['youtube_url'])
    soup = bs4.BeautifulSoup(response.text)
    video_data['views'] = int(re.sub('[^0-9]','',soup.select('.watch-view-count')[0].get_text().split()[0]))
  #  print video_data
    return video_data



def show_video_stats():
    pool = Pool(8)
    video_page_urls = get_video_page_urls()
    urls_file = open("links.html","w") 
    urls_file.write("<html><head><title>Links</title>Links</head><body><table border = 2>")
    i = 0
    for url in video_page_urls:
        if i!=25:
            results = get_video_data(url)
            i+=1
            urls_file.write("<tr>")
            urls_file.write("<td><a href=\""+results['youtube_url']+"\">"+results['title']+"</a></td>")
            urls_file.write("</tr>")
            print(results['title'],i)
    urls_file.write("</table></body></html>")
    urls_file.close()


show_video_stats()
#print get_video_data(get_video_page_urls())
