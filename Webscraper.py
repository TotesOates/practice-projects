import webbrowser

#webbrowser.open('')

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print (len(res.text))

