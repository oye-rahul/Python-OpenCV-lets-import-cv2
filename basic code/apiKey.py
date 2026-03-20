import requests
CityName = input("entr the city name: ")
apikey = "34e6c67a53a39127c97e5cb3287a04c0"
url = f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={apikey}"
response = requests.get(url)
data = response.json()
name = data["name"]
crntlon = data["coord"]["lon"]
crntlat = data["coord"]["lat"]
temp = data["main"]["temp"]
ftemp = temp / 10
weth = data["weather"][0]["main"]
print("-------",name,"-------")
print("lon: ",crntlon,"","lat: ",crntlat)
print("current temp:", round(ftemp, 1))
print("currnt weather:",weth)

