#!/usr/bin/python3
"""Display todo list progress"""

import json
import requests
import sys
if __name__ == "__main__":
    USER_URL = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    res = requests.get(USER_URL)
    user = json.loads(res.text)
    num = sys.argv[1]
    TODO_URL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    res = requests.get(TODO_URL)
    todos = json.loads(res.text)
done = []
for i in todos:
        if i['completed']:
            done.append(i)
print("Employee {} is done with tasks({}/{}):".format(
                                                          user['name'],
                                                          len(done),
                                                          len(todos)))
for i in done:
        print("\t {}".format(i["title"]))