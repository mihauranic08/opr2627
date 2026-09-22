import requests as r

#enumerate
names = ("tadej", "klemen", "sabina", "miha", "andraz")
results = []
age = 0
personS = ""

for person in names:
    results.append((r.get("https://api.agify.io", params={"name": person})).json())

for person in results:
    if person["age"] > age:
        age = person["age"]
        personS = person
print(personS["name"], personS["age"])