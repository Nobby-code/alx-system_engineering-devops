#!/usr/bin/python3
'''python api to return todo list of a given employee id'''

import json

import requests
from sys import argv

if __name__ == "__main__":

    emp_id = argv[1]
    emp_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    todo_url = '{}/{}'.format(emp_url, 'todos')

    '''responses'''
    emp_response = requests.get(emp_url)
    todo_response = requests.get(todo_url)

    ''' object response body '''
    emp_obj = emp_response.json()
    todo_obj = todo_response.json()

    ''' working with file '''
    jsonfile = '{}.json'.format(emp_obj['id'])
    name = emp_obj['username']
    result = []

    for task in todo_obj:
        t = {}
        t['task'] = task['title']
        t['completed'] = task['completed']
        t['username'] = name
        result.append(t)
    with open('2.json', 'w') as f:
        json.dump({emp_obj['id']: result}, f)
