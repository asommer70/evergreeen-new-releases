from flask import Flask
from flask import jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import delegator


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api')
def api():
    base_url = "http://nccardinal.org"
    library_number = 132

    # Get the search page.
    search_url = "/eg/opac/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=" + str(library_number) + "&pubdate=is&date1=&date2=&sort=pubdate.descending"
    r = requests.get(base_url + search_url)

    # Find the .record_title.search_link elements.
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all('a', class_='record_title search_link')
    titles = [title.string.split('[videorecording]')[0].strip() for title in titles]

    # Use subprocesses to get additional info for each title.
    c = delegator.run('')
    
    return jsonify({
        'message': 'Hello, World!',
        'search_url': search_url,
        'titles': titles
    })
