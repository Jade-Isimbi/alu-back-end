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

    done=[]

for todo in todo_response:
    i=0
    if todo['completed']:
          done.append(i)
    print("Employee {} is done with tasks({}/{}):".format(
                                                          USER['name'],
                                                          len(done),
                                                          len(todo)))