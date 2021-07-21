
import requests
import json


resp = requests.get("https://jsonplaceholder.typicode.com/users/1")
d = json.loads(resp.content)


class User:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result


print(User(d))