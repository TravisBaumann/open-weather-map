from sys import argv, exit
import requests

def main():
	try:
		print(argv)
		api_key = argv[1]
	except IndexError:
		print("Please pass in an API key")
		exit(0)

	city = input("For which city do you need weather?\n >")
	country = input("What is the country?\n >")
	location = city + "," + country.lower()



	payload = {
		"appid": api_key,
		"q": location,
		"units": "imperial",
	}

	r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)

	print(r.url)
	weather = r.json()
	
	print("Today's Weather Conditions \n")

	print("Current Temperature: {}".format(weather["main"]["temp"]))
	print("Pressure: {}".format(weather["main"]["pressure"]))
	print("Humidity: {}".format(weather["main"]["humidity"]))
	print("Today's Low: {}".format(weather["main"]["temp_min"]))
	print("Today's High: {}".format(weather["main"]["temp_max"]))

	f = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=payload)

	print(f.url)
	forecast = f.json()

	forecast_list = forecast["list"]

	for index in range(len(forecast["list"])):
		date_variable = (forecast["list"][index]["dt_txt"]).split(" ")
		print(date_variable[0])

	print("Here is the 5-Day Forecast.")



if __name__ == '__main__':
	main()