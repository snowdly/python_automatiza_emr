import requests

response = requests.get('https://geoportal.minetur.gob.es/VCTEL/infoantenasGeoJSON.do?bbox=-3.7048325892838%2C40'
                        '.433671436071%2C-3.7014061138918%2C40.435990772009&zoom=3')
#print(response.json())

for feature in response.json()['features']:
    print(feature)


