#!/usr/bin/python3
'''python api to return todo list of a given employee id'''

import csv

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

    ''' initialization '''
    done_count = 0
    done_tasks = []

    mycsv = '{}.csv'.format(emp_obj['id'])
    name = emp_obj['username']
    with open(mycsv, 'w', newline='') as f:
        for task in todo_obj:
            row = [task['userId'], name, task['completed'], task['title']]
            writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(row)
