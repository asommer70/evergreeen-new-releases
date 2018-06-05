from flask import Flask
from flask import jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import threading
from queue import Queue
import requests


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
request_lock = threading.Lock()
q = Queue()
data_dvds = []


@app.route('/api')
def api():
    base_url = "http://nccardinal.org"
    library_number = 132

    # Get the search page.
    search_url = "/eg/opac/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=" + str(library_number) + "&pubdate=is&date1=&date2=&sort=pubdate.descending"
    res = requests.get(base_url + search_url)

    # Find the .record_title.search_link elements.
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.find_all('a', class_='record_title search_link')
    titles = [title.string.split('[videorecording]')[0].strip()
              for title in titles]

    # Use threads to get additional info for each title.
    for x in range(4):
        t = threading.Thread(target=threader)
        # t.daemon = True
        t.start()

    dvds = []
    for title in titles:
        q.put(title)
        
    dvds.append(q.join())

    #dvds = data_dvds
    #data_dvds = []
    return jsonify(data_dvds)


def threader():
    while True:
        title = q.get()
        #data_dvds.append(search_wiki(title))
        search_wiki(title)
        q.task_done()


def search_wiki(title):
    print('async search_wiki title:', title)
    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=' + title + ' film'

    res = requests.get(url)
    data = res.json()

    hits = []
    for idx, hit in enumerate(data[1]):
        hits.append({
            'title': hit,
            'description': data[2][idx],
            'wiki_url': data[3][idx],
            'image': get_image(hit)
        })

        return hits


def get_image(title):
    url = 'https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&format=json&titles=' + title
    res = requests.get(url)
    data = res.json()

    page_id = [key for key in data['query']['pages']][0]
    image_url = ''
    try:
        image_name = data['query']['pages'][page_id]['pageprops']['page_image']
        
        image_page_url = 'https://en.wikipedia.org/w/api.php?action=query&prop=imageinfo&iiprop=url&format=json&titles=Image:' + image_name
        image_res = requests.get(image_page_url)
        image_data = image_res.json()
        image_page_id = [key for key in image_data['query']['pages']][0]
        image_url = image_data['query']['pages'][image_page_id]['imageinfo'][0]['url']
    except KeyError:
        pass

    return image_url
