import urllib, urllib.parse, urllib.request, urllib.error, json

def google_search_frequency(query):
    """
    Function for validating the semantic of a phrase
    :param query: searched term/phrase
    :return: number of occurrences in the result list of top 10 results
    errors: urllib.error.HTTPError
    """
    api_key = open('.api_key').read()
    service_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': "017576662512468239146:omuauf_lfve",
        'q': query,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    try:
        response = json.loads(urllib.request.urlopen(url).read())
    except Exception as e:
        print(e)
        print(url)
        raise e
    return int(response["queries"]["request"][0]["totalResults"])