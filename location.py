import urllib.request


input = 'old+baneshwor,+Kathmandu'
key='AIzaSyB9i4U1AFlnh5p0eFkQtK-csvzaDUq9h1g'
link = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input={}&key={}&sessiontoken=1234567890".format(input, key)

contents = urllib.request.urlopen(link).read()
