import urllib.request, json
from .models import Quote, Blog



#get base url
base_url = None


def configure_request(app):
    global base_url
    base_url = 'http://quotes.stormconsultancy.co.uk/random.json'


def get_quotes():
    '''
    Function that gets json response the url request
    '''
    with urllib.request.urlopen(base_url) as url:
      returned_data = url.read()
      response = json.loads(returned_data)

      return response


def process_results(response):
    '''
    function that processes the quote result
    '''
    if response:
       id  = response['id']
       author = response['author']
       quote = response['quote']
    else:
        id = 1
        author = 'Mandela'
        quote = 'We are who we think we are'

    new_quote = Quote(id, author, quote)

    return new_quote



