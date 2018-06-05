import threading
import requests
from queue import Queue


request_lock = threading.Lock()
q = Queue()
dvds = []


def main():

    titles = [
        'Ferdinand',
        'Victoria. The complete second season',
        'The man who invented Christmas',
        'Black Panther',
        'Star Wars. The last Jedi',
        'Coco',
        'The shape of water',
        'All the money in the world',
        'The breadwinner',
        'The Post'
    ]

    for x in range(4):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.return_queue = q
        t.start()
        # print('main t.return_queue.get():', t.return_queue.get())

    for title in titles:
        q.put(title)
    q.join()
    print('main dvds:', dvds)


def search_wiki(title):
    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=' + title + ' film'

    with request_lock:
        res = requests.get(url)
    print('title:', title, 'res.json()[0]:', res.json()[0])
    data = res.json()

    hits = []
    for idx, hit in enumerate(data[1]):
        hits.append({
            'title': hit,
            'description': data[2][idx],
            'wiki_url': data[3][idx]
        })

    return hits

def threader():
    while True:
        title = q.get()
        dvds.append(search_wiki(title))
        q.task_done()
        # return hits
        # print('threader hits:', hits)


if __name__ == '__main__':
    main()
