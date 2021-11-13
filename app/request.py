from app import app
import urllib.request, json
from .models import quote


Quote = quote.Quote

#get base url
base_url = app.config['QUOTE_BASE_URL']


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
        auhtor = 'Mandela'
        quote = 'We are who we are'

    new_quote = Quote(id, author, quote)

    return new_quote