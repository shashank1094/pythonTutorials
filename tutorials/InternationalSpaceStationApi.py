# This includes how to use data from ISS .
# Link to the tutorial is here :
# https://www.dataquest.io/blog/python-api-tutorial/
import requests

# Current location of ISS :
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
# Print the status code of the response.
print("Response code is : " + str(response.status_code) + "\nResponse is : " + response.text)

print("\n\n")
# When will ISS be above specific location :
# My location lat & long are : 28.594133, 77.031621
# Set up the parameters we want to pass to the API.
parameters = {"lat": 28.59, "lon": 77.03}
# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# Print the content of the response (the data the server returned)
print(response.content)
# print(response.content.decode("utf-8"))
# You may have noticed that the content of the response earlier was a string (although it was shown as a
# bytes object, we can easily convert the content to a string using response.content.decode("utf-8")).
# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=28.59&lon=77.03")
print(response.content)
# print(response.json())

print("\n\n")
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
# 9 people are currently in space.
print(data["number"])
print(data)
print("\n\n")
allPeople = data["people"]
for people in allPeople:
    print(people["name"] + "is on " + people["craft"] + ".\n")


