import requests



def get_exact_timezone(place):
    username = 'tutorbin'
    url = 'http://api.geonames.org/searchJSON?style=full&maxRows=1&name_equals={0}&username={1}'.format(place,username)
    response = requests.get(url).json()
    return response['geonames'][0]['timezone']['timeZoneId']


print(get_exact_timezone('illinois'))