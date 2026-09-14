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