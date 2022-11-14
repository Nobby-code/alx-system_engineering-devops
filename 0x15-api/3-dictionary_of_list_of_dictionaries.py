#!/usr/bin/python3
'''python api to return todo list of all employees'''

import json

import requests
from sys import argv

if __name__ == "__main__":

    users_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    emp_obj = requests.get(users_url).json()
    todo_obj = requests.get(todo_url).json()

    total = {}

    for user in emp_obj:
        _id = user['id']
        result = []

        for todo in todo_obj:
            if _id == todo['userId']:
                task = {}
                task['task'] = todo['title']
                task['completed'] = todo['completed']
                task['username'] = user['username']
                result.append(task)
        total[_id] = result
    with open('todo_all_employees.json', 'w') as f:
        json.dump(total, f)
