import requests
"""
# dictionary

dictionary = {
    "key" : "value",
    "key2" : "value2"
}
print(dictionary["key"])

#mixed

mixed = {
    "number" : 17,
    "name" : "Miha",
    "classmates" : ["Luka", "Marko"],
    "dictionary" : {
        "corpo" : "Dacia",
        "power" : "120w"
    }
}

print(mixed["dictionary"]["corpo"])

#Open Meteo API
import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=rain_sum&hourly=rain"
call = requests.get(base_url).json()
print(call["daily"]["rain_sum"])
"""
#Exercises
#https://hackmd.io/@lukac/api1
#1.
#base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"
#call = requests.get(base_url).json()
#print(call["current"]["temperature_2m"])

#2.
base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"
call = requests.get(base_url).json()
#print(call["daily"]["temperature_2m_min"], call["daily"]["temperature_2m_max"])

#3.
maximum = call["daily"]["temperature_2m_max"].index(max(call["daily"]["temperature_2m_max"]))
minimum = call["daily"]["temperature_2m_min"].index(min(call["daily"]["temperature_2m_min"]))
print(call["daily"]["time"][maximum], call["daily"]["time"][minimum])