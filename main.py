import requests
import json
import win32com.client as w

city = input("Enter the name of the city : ")

url = f"http://api.weatherapi.com/v1/current.json?key=7dcc669906be484cb81140044233003&q={city}"

r = requests.get(url)
weatherdic = json.loads(r.text)
s = weatherdic["current"]["temp_c"]
speaker = w.Dispatch("SAPI.SpVoice")
print(f"The current weather in {city} is {s} degrees")
speaker.Speak(f"The current weather in {city} is {s} degrees")
print("***END***")