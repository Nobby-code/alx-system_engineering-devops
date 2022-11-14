#!/usr/bin/python3
'''python api to return todo list of a given employee id'''
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

    for task in todo_obj:
        if task['completed'] is True:
            done_count += 1
            done_tasks.append(task['title'])

    data = 'Employee {} is done with tasks({}/{}):'
    print(data.format(emp_obj['name'], done_count, len(todo_obj)))
    for done in done_tasks:
        print('\t {}'.format(done))
