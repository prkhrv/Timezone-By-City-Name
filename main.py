import requests


google_key = "" #ADD YOUR API KEY HERE
def get_coordinates(place):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&sensor=false&key={1}'.format(place,google_key)
    response = requests.get(url).json()
    print(response)

def get_exact_timezone(place):
    username = 'tutorbin'
    url = 'http://api.geonames.org/searchJSON?style=full&maxRows=5&name_equals={0}&username={1}'.format(place,username)
    response = requests.get(url).json()

    tzinfo = []
    for i in range(0,len(response['geonames'])):
        data = {
            "country": response['geonames'][i]['countryName'],
            "tz": response['geonames'][i]['timezone']['timeZoneId'],
            "countryCode": response['geonames'][i]['countryCode'],
        }

        tzinfo.append(data)


    return tzinfo


print(get_exact_timezone('san francisco'))
# get_coordinates('california,USA')