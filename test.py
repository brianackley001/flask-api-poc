import requests

BASE = "http://127.0.0.1:5000/"

data = [
  {"likes": 15, "name": "How to do things", "views":223},
  {"likes": 255, "name": "How to not break things", "views":1000},
  {"likes": 500, "name": "How to search for things", "views":5783}
]

# for i in range(len(data)):
#   response = requests.put(BASE + "video/" + str(i), data[i])
#   print(response.json())

# input()

# response = requests.delete(BASE + "video/0")
# print(response)
# input()


# response = requests.get(BASE + "video/2")
# print(response.json())

response = requests.patch(BASE + "video/1", {'likes': 23456, 'name': 'Some Random Video Title'})
print(response.json())